# app.py 코드 실행하고 명령프롬프트에 cd app.py폴더경로 입력
    # -> dir 입력해 app.py 들어있는 폴더에 잘 들어갔는지 확인
    # -> python app.py 입력해 서버 열기

# get 방식
# @app.route('/') 결과 보기 -> 크롬 주소란에 http://127.0.0.1:5000/ 입력
# @app.route('/second') 결과 보기 -> 크롬 주소란에 http://127.0.0.1:5000/second 입력


# 라이브러리 로드
from flask import Flask, render_template, request, redirect
# flask 라이브러리, Flask 클래스, render_template 함수,
# request 함수(요청에 대한 내용을 가지고 있음. requests 아님 주의.),
# redirect 함수(특정한 주소로 이동하는 기능)

import pandas as pd

# render_template() 함수
#   -> html 문서를 불러와 문자형으로 변환하는 기능
# html 문서에서 {{ python 코드 }}, {%= 변수명 %} 에 해당하는 부분을 찾아 형태 변환
# html 문서를 불러오는 기본 경로: 현재 경로에서 templates 하위 폴더

# Flask class 생성
#   -> 웹 서버를 구축하는 기능
# 해당 class 생성 시 호출되는 생성자 함수
    # 필수 인자 1개: 현재 파일의 이름(app.py)
    # __name__ : 파일의 이름을 문자 형태로 넣어줌
app = Flask(__name__)


# route 함수 = 네비게이션 함수
# base url(기본 주소): 127.0.01:5000  -> 어디에서 실행하느냐에 따라 바뀔 수 있음.
# route( {주소값(상대 주소)} ) -> base_url + 상대 주소
    # -> 요청이 들어왔을 때 바로 아래의 함수와 연결(호출)
# @app.route('/')와 @app.route('/second')의 함수 이름이 같으면 Error 발생
@app.route('/')
def index():
    # return "Hello_world"
    return render_template('index.html')

@app.route('/second')
def second():
    # return "<a href='http://www.google.com'>Google</a>"
    # 페이지 하나의 html 태그를 모두 이 파일에서 작성하면 너무 길어지고 비효율적.
    # 따라서 실제 html 파일로 만들어 페이지 하나하나씩 관리.
    # templetes 폴더 만들어 html 파일 생성해 불러와서 되돌려준다.
    # print를 사용해 유저가 보낸 데이터 확인
    # 데이터를 get 방식으로 보내면 request 안의 args 안에 데이터가 존재
    # request.args는 dict 형태의 데이터
    print(request.args)
    _text = request.args['input_text']
    _pass = request.args['input_pass']
    print(f'유저가 입력한 text는 {_text}이고 password는 {_pass}이다.')
    # _text가 'test'이고 _pass가 '1234'와 같다면 로그인 성공
    # second.html을 보여준다.
    if (_text == 'test') & (_pass == '1234'):
        df = pd.read_csv('../csv/aapl.csv').head(10)
        # df를 dict 형태로 변환 (list 안의 dict 형태)
        data = df.to_dict(orient='records')
        # columns의 목록을 html로 보낸다.
        cols = list(df.columns)
        # x축의 데이터를 list 형태로
        x = df['Date'].to_list()
        y = df['Adj Close'].to_list()
        return render_template('second.html',
                               table_data = data,
                               cols = cols,
                               x_data = x,
                               y_data = y)
    else:
        # 로그인 페이지(127.0.0.1:5000/)로 되돌아간다.
        return redirect('/')

@app.route('/third', methods=['post'])
def third():
    print(redirect)
    # post 방식으로 데이터를 보내면
    # request 안의 form 에 데이터 존재
    _text = request.form['input_text']
    _pass = request.form['input_pass']
    print(f'유저가 입력한 text는 {_text}이고 password는 {_pass}이다.')
    return ""


# 웹 서버를 시작하는 함수 run()
# 매개변수
    # host : 허용 주소 목록 (기본값 - 로컬 PC만 접속. 0.0.0.0 으로 변경 시 모든 주소 접속 가능.)
        # 기본적으로는 모두가 들어올 수 있지만, 특정 주소를 써두면 허용된 주소만 들어올 수 있다.
    # port : 해당 웹서버의 지정되는 포트 번호 (기본값 - 5000)
    # debug : 디버그모드 on/off (기본값 - off(False))
        # 중간에 소스코드 수정, 저장했는데 Error 발생한 채로 서버 돌아가면 곤란
        # 디버그모드 on 시 유저들은 구버전 그대로 사용, 나는 수정 가능
        #   => 저장하고 ctrl+c로 서버 종료했다 켤 필요 없이, 저장하면 알아서 반영됨
app.run(debug=True)


# 유저와 서버 간의 데이터 주고받기  (ex. 로그인)
# 데이터를 주고받을 때의 데이터 타입 = dict
# 데이터 보내는 방식(주소 생성 방식) -> get 또는 post
# 유저가 보낸 데이터를 서버가 확인 -> 요청 메시지 안에 데이터가 존재


# get이 기본적인 구조라 더 빠르지만 보안에 취약. 주소만 쳐도 들어갈 수 있음.
# post는 보안에 더 강하지만 첫 메인페이지에 모든 사람이 접근 불가.