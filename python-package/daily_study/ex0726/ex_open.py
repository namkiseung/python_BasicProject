# -*- coding: cp949 -*-

##f = open("i2sec.txt","w")
##for i in range(10):
##    f.write('{} \n'.format(i))
##f.close()


##with open("i2sec.txt", "a") as f: 
##    for i in range(30):
##        f.write('{} \n'.format(i))
##        f.write( chr(ord('a')+i) )
    
##f = open("C:\Users\student\Desktop\hosts","a") #���� ���� �߰��ϱ� (�����ϱ�)
####for i in range(2,10):
####    for j in range(1,10):
####        f.write('{} * {} = {}\n'.format(i,j,i*j))
##f.write('\n127.0.0.1 www.google.com')
##f.close()


##import requests #���� ������Ʈ�ؼ� (�����ϱ�)
##
##res=requests.get("http://www.naver.com")
##f = open('tmp_naver','w')
##f.write(res.content)
##f.close()


##f = open("C:/Users/student/Desktop/hosts","r") #���� �б�(�ҷ�����)
##data = f.read()
##print data
##f.close()
'''
f = open("C:/Users/student/Desktop/hosts", "r")
import sys
while True:
    sen = f.readline()    
    if not sen:#    if f.readline() == '127.0.0.1 www.google.com': 
        break
    print sen
#        f.close()
'''
#f = open("C:/Users/student/Desktop/hosts","r")
#lines = f.readlines()
#print '{}'.format(lines)
##f.seek(10)
##f.close()


f_hosts_copy = open("C:/Users/student/Desktop/hosts","r")
while True:
    read=f_hosts_copy.readline()
    print read.split()
    if read == '#      102.54.94.97     rhino.acme.com          # source server\n':
        break    
f_hosts_copy.close()

