import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from datetime import datetime

url = 'https://comp.wisereport.co.kr/company/c1010001.aspx?cmp_cd='

# 종목코드
# SK하이닉스, 삼성전자, Yes24
# codes = ['000660', '005930', '053280']
codes = []
# 유저가 입력한 값을 codes에 추가
# 최대 codes의 개수는 10개
# 유저가 입력한 값이 존재하지 않으면 추가 작업도 종료
for i in range(10):
    # 유저가 값을 입력한다.
    input_code = input('검색하려는 종목의 코드를 입력하시오: ')
    # input_code가 존재하지 않는다면 반복문 종료
    if input_code:
        codes.append(input_code)
    else:
        break

# 또는
# while True:
#     input_code = input('검색하려는 종목의 코드를 입력하시오: ')
#     if input_code:
#         codes.append(input_code)
#         if len(codes) == 10:
#             break


# 빈 데이터프레임 생성
df = pd.DataFrame()

# codes 만큼 반복 실행 -> 결과는 데이터프레임
# -> 하나의 데이터프레임으로 결합(추가) -> csv 파일로 저장
for code in codes:
    # url과 code를 이용해 요청
    res = requests.get( url+code )
    # 응답 데이터를 BeautifulSoup을 이용해 파싱
    soup = bs(res.text, 'html.parser')
    # 종목의 코드가 잘못된 경우
    try:
        cmp_info = list(
            map(
                lambda x: x.get_text(),
                soup.find(
                    'div', attrs={'class':'cmp_comment'}
                ).find_all('li')
            )
        )

        cmp_etc = list(
            map(
                lambda x: x.get_text(),
                soup.find(
                    'div', attrs={'class':'cmp_comment_etc'}
                ).find_all('li')
            )
        )
    except Exception as e:
        print(e)
        # 종목 코드가 잘못되었을 때 다음 종목코드로 이동
        continue

    code_df = pd.DataFrame(
        {
            'cmp_info': cmp_info,
            'cmp_etc': cmp_etc
        }
    )
    # code_df에 code 컬럼을 추가하여 code값을 대입
    code_df['code'] = code
    # df에 code_df 추가 -> 단순한 행의 결합 -> concat() 함수 이용
    # concat()은 df가 아닌 pandas에서 호출해야 함
    # pandas는 라이브러리라서 바로 저장되지는 않음 -> df에 저장해야 함
    df = pd.concat([df, code_df], axis=0)
    # 서버에 과부하가 걸리지 않게 잠깐씩 텀 주어야 함 = 에티켓!!!
    time.sleep(1)
    # 반복 실행될 때마다 로그를 추가해 진행 상황 확인
    print(f'{code} 데이터 수집 완료')

# 현재 시간을 불러온다.
now_time = datetime.now()  # 현재 시간을 나노초까지 표시
now_str = now_time.strftime('%Y%m%D_%H%M%S')  # 현재 시간의 포맷을 '년월일_시분초'로 변경

# df를 csv 파일로 저장
df.to_csv(f'wise_data{now_time}.csv', index=False)

# 터미널 여러 개 열려있으면 충돌 발생하므로 쓰고 나면 닫아주기
# 휴지통 모양의 'kill terminal' 버튼