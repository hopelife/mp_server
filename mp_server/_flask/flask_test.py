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

if __name__ == "__main__":
    ## NOTE: post test
    # data = {
    #     "user_id": "test01",
    #     "user_name": "테스트01"
    # }
    data = {}
    url = "http://127.0.0.1:6868/create"
    # data = {'param1': 'value1', 'param2': 'value'}
    res = requests.post(
        url, 
        data = {'a': 'b'}, 
        # headers = {'Content-Type': 'application/json; charset=utf-8'}
    )
    print(f"res.text: {res.text}")