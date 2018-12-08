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
    print('''########################PASSWORD MANAGE PROGRAM Console Box\n[1] READ \n[2] CREATE  \n[3] UPDATE \n[4] DELETE\n########################''')
    pass 

def read(data=''): #CRUD comment
    print("검색을 원하면 문자열을 입력해주세요.\n")
    while True:        
        temp_list=[]
        if data not in temp_list:
            return 'None'
        else:
            pass
    pass

def create_comment(): #CRUD comment
    return "Enter the following \n(1)Site-Name | (2) Site-URL | (3) UserID | (4) UserPW \n"

def get_list_all():
    print("#############Site List in DateBase table########################")
    for x in select_user():        
        print("num : %d  |  hostname : %s | hostURL : %s | ID : %s | Date : %s |" % (x[0], x[1], x[2], x[3], x[6]))
    print("########################################################")
    pass
def get_list_pw(t_name):
    print("#############Site List in DateBase table########################")
    x=select_user_pw(t_name)
    print("RESULT : num : %d  |  hostname : %s | hostURL : %s | ID : %s | PW : %s | Date : %s |" % (x[0], x[1], x[2], x[3], x[4].translate({ ord('4'): '@' }), x[6]))
    print("########################################################")
    pass

if __name__=="__main__":
    num_list=[1,2,3,4,5,6,7,8,9]
    while True:
        print(open_comment())
        select_num=input(">>")
        if str(select_num) == str(1): #READ of CRUD
            try:
                get_list_all()
                temp=input(">> site name : ")
                if temp != '' and temp != None: 
                    get_list_pw(temp)
                elif temp == "0" and temp == 0:
                    pass
                else:
                    pass
            except:
                pass
            finally:
                pass
        elif str(select_num) == str(2): #CREATE of CRUD
            print(create_comment())
            _site_name=input(">> Site name : ")
            _site_url=input(">> Site url : ")
            _user_id=input(">> UserID : ")
            _user_pw=input(">> UserPW : ")            
            insert_user(__site_name=_site_name, __site_url=_site_url, __user_id=_user_id, __user_pw=_user_pw, __content='')
            #변경된 표준출력
            print("output : {} \noutput : {} \noutput : {} \noutput : {} \n".format(_site_name,_site_url, _user_id, _user_pw))
        elif str(select_num) == str(3): #UPDATE of CRUD
            #get_list_all()  #list all
            __h_name=input(">> hostname : ") #입력받은 ID검증 후 수정 ok
            update_info(__h_name)
            #변경된 내용출력 -> 이메일 or 표준출력
            #print("output : {} \noutput : {} \noutput : {} \noutput : {} \n".format(__site_name,__site_url, __user_id, __user_pw))
        elif str(select_num) == str(4): #DELETE of CRUD
            get_list_all()
            del_num = input("What number do you want to delete? >>")            
            if del_num != '' and del_num != None: 
                del_text=input("Enter the word as it is. \"DELETE\" : ")
                if del_text != "DELETE":
                    print("[+] failed Removed")
                    break
                else:
                    #삭제
                    delete_site(del_num)
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
    
    
    
    
    
        
        
        
        

        
        
        
