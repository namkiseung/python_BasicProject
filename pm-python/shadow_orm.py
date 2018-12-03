from sqlite_orm.database import Database
from sqlite_orm.field import IntegerField, BooleanField, TextField
from sqlite_orm.table import BaseTable
from passlib.hash import pbkdf2_sha256
from  desc_manage import *
#from time import ctime
import logging, os
import settime
'''
선택한 데이터베이스에 대한 연결(connection)을 설정
데이터 전달을 위한 커서(cursor)를 생성
SQL을 이용해 데이터를 조작(상호작용)
SQL 조작을 데이터에 적용한 후 이를 영구적으로 반영하거나(커밋) 그러한 조작을 중단시켜(롤백) 상호작용이 발생하기 전의 상태로 데이터를 되돌리도록 연결에 지시
데이터베이스에 대한 연결을 닫음(close)
'''
def open_comment(): #CRUD comment
    print('''########################PASSWORD MANAGE PROGRAM Console Box\n[1] READ \n[2] CREATE  \n[3] UPDATE \n[4] DELETE########################''')
    pass 

def read(data=''): #CRUD comment
    print("검색을 원하면 문자열을 입력해주세요.\n")
    while True:        
        temp_list=[]
        if data not in temp_list:
            return 'None'
        else:
            pass
    pass#'''#############[1] SELECT Site-name \n[2] SELECT userID########################'''

def create_comment(): #CRUD comment
    return "Enter the following \n(1)Site-Name | (2) Site-URL | (3) UserID | (4) UserPW \n"

def get_list():
    print("#############Site List in DateBase table########################")
    return '''[1] gabia \n[2] naver \n[3] daum \n[4] google \n[5] lol \n[6] i2sec \n[7] samsung \n[8] LG \n[9] NIT service \n[10] SK infosec \n[11] A3 \n[12] Cyberone'''

if __name__=="__main__":
    while True:
        print(open_comment())
        select_num=input(">>")
        if str(select_num) == str(1): #READ of CRUD
            print(get_list())
            temp=input(">>")
            #print(read(temp))
        elif str(select_num) == str(2): #CREATE of CRUD
            print(create_comment())
            __site_name=input(">> Site name : ")
            __site_url=input(">> Site url : ")
            __user_id=input(">> UserID : ")
            __user_pw=input(">> UserPW : ")
            #변경된 표준출력
            print("output : {} \noutput : {} \noutput : {} \noutput : {} \n".format(__site_name,__site_url, __user_id, __user_pw))
        elif str(select_num) == str(3): #UPDATE of CRUD
            print(get_list())
            print(">> Site name : %s" % ("test site name"))
            print(">> Site url : %s" % ("test site url"))
            __user_id=input(">> UserID : ") #입력받은 ID검증 후 수정 ok
            __user_pw=input(">> UserPW : ")
            #변경된 내용출력 -> 이메일 or 표준출력
            print("output : {} \noutput : {} \noutput : {} \noutput : {} \n".format(__site_name,__site_url, __user_id, __user_pw))
        elif str(select_num) == str(4): #DELETE of CRUD
            print(get_list())
            del_num = input("Enter the number to Delete >>")
            if del_num in [str(1),str(2)]:
                del_text=input("Follow Text : \"DELETE\" >>")
                if del_text != "DELETE":
                    break
                else:
                    #삭제
                    print("[+] Success Removed")
                    pass
            else:
                break
            #삭제할 인덱스 받고 존재한다면 "delete 문자열 입력받기"
                 #delete문자열 맞으면-> 삭제실행  // 틀리면 뒤로가기
            #삭제할 인덱스 옳지 않으면 뒤로가기
            pass
        else:
            quit()
    
    
    
    
    
        
        
        
        

        
        
        
