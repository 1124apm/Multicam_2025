import pandas as pd
import time
import re
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sqlalchemy import create_engine

# 아래 코드들 쓰면 크롬 켜는 게 좀 빨라짐. 필요하면 복붙 (여기부터)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
# header setting 변경
opts.add_argument('--headless=new')
opts.add_argument('--disalble-gpu')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument('--no-sandbox')
opts.add_argument('--window-size=1920,1080')
# 프록시/언어 고정
opts.add_argument('--lang=ko-KR')

# (여기까지)


search_item = input('검색어를 입력하시오 :')
save_type = input('저장 방식을 지정하시오 (csv / DB) :')

# 검색어가 잘 들어왔는지 확인 -> 안 들어왔으면 다시 입력
while True:
    if len(search_item) == 0:
        search_item = input('검색어를 입력하시오 :')
    else:
        break

while True:
    if save_type in [ 'csv', 'CSV', 'db', 'DB' ]:
        break
    else:
        save_type = input('저장 방식을 지정하시오 (csv / DB) :')

driver = webdriver.Chrome( service=Service(
            ChromeDriverManager().install()
            ), options= opts
        )
driver = webdriver.Chrome()

# 로딩 시간을 위해, 페이지에 변화가 일어날 때마다 딜레이를 추가한다.
time.sleep(1)
# driver로 네이버에 요청을 보낸다.
driver.get('https://naver.com')
time.sleep(1)
# id가 query인 태그 선택
search_element = driver.find_element(By.ID, 'query')

# 검색어 입력
search_element.send_keys(search_item)
# 검색어 창에 Enter 이벤트 발생
search_element.send_keys(Keys.ENTER)
time.sleep(1)

# 쇼핑 문구가 있는 하이퍼링크를 선택하여 클릭한다.
driver.find_element(By.LINK_TEXT, '쇼핑').click()
time.sleep(1)

# driver에서 탭을 이동한다.
driver.switch_to.window(
    driver.window_handles[1]
)

# 스크롤을 조금씩 끝까지 내린다.
while True:
    # driver의 스크롤의 현재 높이
    last_height = driver.execute_script('return window.pageYOffset')

    # driver에서 스크롤을 일정 간격으로 내린다.
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(3)

    # 스크롤 이동 후 현재 높이
    new_height = driver.execute_script('return window.pageYOffset')

    # 스크롤의 현재 높이 = 내린 높이라면 끝까지 내려간 것이니 반복문 종료
    if new_height == last_height:
        break

# driver에 있는 html 문서를 변수에 저장
html_data = driver.page_source
# selenium의 역할 끝 -> driver를 종료
driver.quit()

# 해당 페이지의 html 문서를 저장
# BeautifulSoup을 이용해서 데이터 파싱
soup3 = bs(html_data, 'html.parser')
# 광고 상품을 제외한 모든 상품의 이름과 가격, 링크 주소를 2차원 데이터로 생성
content_data = soup3.find('div', attrs={'id':'content'})
div_list = content_data.find_all('div', attrs={'class': re.compile('product_item')})
# 특정 이름이 포함된 div 차기
values = []
for div_data in div_list:
    item_name = div_data.find('div', attrs={'class' : re.compile('product_title')}).get_text()
    item_price = div_data.find('span', attrs={'class':'price'}).get_text()
    item_url = div_data.find('a')['href']
    dict_data = {'상품명': item_name, '가격': item_price, 'url': item_url}
    values.append(dict_data)

# 생성된 2차원 데이터를 데이터프레임으로 생성
df = pd.DataFrame(values)
print(df)
print('저장 방식:', save_type)

if save_type == 'csv':
    # 검색어('아이폰')를 파일명으로 csv 파일을 생성하고 인덱스는 제외한다.
    df.to_csv(f'{search_item}.csv', index=False)
else:
    engine = create_engine(
        'mysql+pymysql://root:1408@localhost:3306/multicam'
    )
    df.to_sql(
        name= search_item,
        con= engine,
        if_exists= 'replace',
        index= False
    )