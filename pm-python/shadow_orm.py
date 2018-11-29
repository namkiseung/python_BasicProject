from sqlite_orm.database import Database
from sqlite_orm.field import IntegerField, BooleanField, TextField
from sqlite_orm.table import BaseTable
from passlib.hash import pbkdf2_sha256
from  desc_manage import Manage
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

def insert_user(__site_name, __site_url, __user_id, __user_pw, __content=''):
    with Database(os.getcwd().replace("\\","/")+"/shadow.db") as db:
        #데이터베이스 객체 생성
            user1 = Manage(site_name=__site_name,site_url=__site_url,user_id=__user_id,user_pw=__user_pw,content=__content,date=settime.get_time())
        #데이터베이스 객체 insert
            db.query().insert(user1).execute()
    pass

def select_user(input_id=''):
    with Database(os.getcwd().replace("\\","/")+"/shadow.db") as db:
    #select 출력문        
        for row in db.query(Manage).select().execute():            
            print(row)
        #print(pbkdf2_sha256.hash("asd"))
    return ''
def create_db():
    with Database(os.getcwd().replace("\\","/")+"/shadow.db") as db:
    #테이블 생성
        db.query(Manage).create().execute()
    pass

if __name__=="__main__":    
    #logger configure:
    logging.basicConfig(filename=os.getcwd().replace("\\","/")+"/error.log", level=logging.DEBUG, format=('%(asctime)s: '
                                                                            '%(filename)s: '
                                                                            '%(levelname)s: '
                                                                            '%(funcName)s(): '
                                                                            '%(lineno)d: '
                                                                            '%(message)s'), datefmt="%Y-%m-%d %H:%M:%S")
    #create_db()
    #insert_user(__site_name="i2sec", __site_url="i2sec.co.kr", __user_id="rltmd", __user_pw="0000")
    print()
    #select_user()
    
    
        
        
        
        

        
        
        
