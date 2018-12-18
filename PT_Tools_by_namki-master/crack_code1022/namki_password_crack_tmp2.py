#-*- coding:utf-8 -*-
import requests

# 로그인할 유저정보를 넣어주자 (모두 문자열)
LOGIN_INFO = {
    "user_id" : "i2sec",
    "user_pw" : "0000"
}
header = {"User-agent":"Mozilla/5.0"}
for x in range(4):
    # Session 생성, with 구문 안에서 유지
    with requests.Session() as s:
        # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
        login_req = s.post('http://192.168.177.132:1111/', data=LOGIN_INFO)
        #print login_req.headers
        print login_req.is_redirect
        
        #print login_req.history
        print(login_req.status_code)
        
#https://wikidocs.net/4126        
        
        
        
