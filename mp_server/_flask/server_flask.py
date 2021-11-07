# -*- coding=utf-8 -*-
"""
주요 기능: 
    - 매매 신호 수신
    - 매매 결과 송신
    - 사용자 인증

사용례: 
    - 
"""

##@@@ 모듈 import
##============================================================

##@@ Built-In 모듈
##------------------------------------------------------------
import os, sys
import requests
import time
import json

##@@ Package 모듈
##------------------------------------------------------------
# from flask import Flask
from flask import Flask, render_template, request

##@@ User 모듈
##------------------------------------------------------------
# sys.path.append(os.path.join(os.path.dirname(__file__), '../../Assistant/Message'))
# from Slack import Slack

##@@@ 전역 상수/변수
##============================================================

##@@ Section
##------------------------------------------------------------



##@@@ 보조 함수
##============================================================

##@@ Section
##------------------------------------------------------------



##@@@ 실행 함수
##============================================================

##@@ Section
##------------------------------------------------------------


# ##@@ flask_api
# ##------------------------------------------------------------
# import os, sys
# from flask import Flask
# sys.path.append(os.path.join(os.path.dirname(__file__), '../../Assistant/Message'))
# from Slack import Slack

# app = Flask (__name__)
 
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/slack')
# def send_slack():
#     s = Slack()
#     message="Message from Slack by Flask API Server"
#     s.send_message_simple(message=message)

#     return message


# ##@@ flask_test
# ##------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello World!"


@app.route('/hi/<name>')
def hi(name):
    return f"Hi! {name}"


# @app.route('/create', methods=['POST'])
# def create():
#     # print(request.is_json)
#     params = request.get_json()
#     # print(params)
#     # print(params['user_id'])
#     # return {"test": "test"}
#     return params

@app.route('/handle_post', methods=['POST'])
def handle_post():
    params = json.loads(request.get_data(), encoding='utf-8')
    if len(params) == 0:
        return 'No parameter'

    params_str = ''
    for key in params.keys():
        params_str += 'key: {}, value: {}<br>'.format(key, params[key])
    return params_str


@app.route('/send_post', methods=['GET'])
def send_post():
    params = {
        "param1": "test1",
        "param2": 123,
        "param3": "한글"
    }
    res = requests.post("http://127.0.0.1:6868/handle_post", data=json.dumps(params))
    return res.text


# @app.route('/',methods=('GET', 'POST')) # 접속하는 url
# def index():
#     if request.method == "POST":
#         # user=request.form['user'] # 전달받은 name이 user인 데이터
#         print(request.form.get('user')) # 안전하게 가져오려면 get
#         user = request.form.get('user')
#         data = {'level': 60, 'point': 360, 'exp': 45000}
#         return render_template('index.html', user=user, data=data)
#     elif request.method == "GET":
#         user = "반원"
#         data = {'level': 60, 'point': 360, 'exp': 45000}
#         return render_template('index.html', user=user, data=data)


if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port=4545)
    app.run(debug=True, host='127.0.0.1', port=6868)

    ## NOTE: post test
    # browser:: http://127.0.0.1:6868/send_post
