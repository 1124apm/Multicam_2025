from flask import Flask, request, render_template, url_for
import pandas as pd

# __name__ : 현재 파일의 이름
app = Flask(__name__)

# ====================================================
# 웹서버를 사용할 주소들의 목록

# base_url + '/' 주소로 요청이 들어왔을 때, 바로 아래의 함수를 호출
    # 현재 base_url은 127.0.0.1:5000
# 함수를 생성할 때, 함수의 이름은 중복될 수 없음을 유의
@app.route('/')
def index():
    # 샘플 데이터프레임 로드
    # 현재 경로 - static 폴더 - data 폴더 - AAPL.csv
    df = pd.read_csv('static/data/AAPL.csv')
    # 하위의 데이터 30개만 필터
    df = df.tail(30)
    # index.html에서 table에 컬럼의 이름들을 사용하기 위해 list 형태의 columns 생성
    cols = list(df.columns)
    # table에 데이터의 값들을 [{}, {}, {}] 형태로 생성
    # chart에서 사용할 x축의 데이터와 y축의 데이터를 list 형태로 생성
        # df의 type이 DataFrame, df['Date']는 Series. -> DataFrame과 Series 안에 to_list() 함수 존재
        # df.columns의 type은 인덱스이므로 to_list() 함수가 존재하는지 모르니 list로 묶어줌
    x = df['Date'].to_list()
    y = df['Volume'].to_list()
    values = df.to_dict(orient='records')
    # 현재 작업 경로에서 하위 디렉토리인 templates 안에 있는 index.html을 되돌려준다.
    # bootstrap 홈피에서 다운받은 샘플에서
    #   bootstrap-5.3.8-examples\dashnoard\index.html을 templates로 복붙
    # cols와 values를 이용해 index.html에서 tabel 태그 생성
    return render_template('index.html',
                           cols= cols,
                           values= values,
                           x= x,
                           y= y)

@app.route('/second')
def second():
    # AAPL 로드
    df = pd.read_csv('static/data/AAPL.csv')
    df = df.tail(30)
    cols = list(df.columns)
    values = df.to_dict(orient='records')
    x = df['Date'].to_list()
    y = df['Adj Close'].to_list()
    return render_template('index2.html',
                           cols= cols,
                           values= values,
                           x= x,
                           y= y)

@app.route('/third')
def third():
    # AAPL 데이터에서 y축의 데이터를 2개(저가, 고가) 사용
    df = pd.read_csv('static/data/AAPL.csv')
    df = df.tail(30)
    cols = list(df.columns)
    values = df.to_dict(orient='records')
    x = df['Date'].to_list()
    y = df['Low'].to_list()
    y2 = df['High'].to_list()
    return render_template('index3.html',
                           # 꼭 변수명을 cols, values, x, y로 쓸 필요 없음
                           columns= cols,
                           value_data= values,
                           date= x,
                           low_data= y,
                           high_data= y2)

# refer 폴더에 각각의 파트를 따로 저장해놨기 때문에,
#  refer 폴더의 파일 중 하나만 수정해도 그 부분이 모든 index 파일에서 일괄적으로 수정된다.

# 웹 서버 실행
# debug=True : 파일이 저장될 때마다 웹서버를 자동으로 재시작
app.run(debug=True)

# 명령 프롬프트에 'cd 현재경로' 입력 -> 'python app.py' 입력 -> 서버 구동
# 크롬 주소란에 'http://127.0.0.1:5000/' 입력하면 열린 서버로 이동