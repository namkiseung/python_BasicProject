from sqlite_orm.database import Database
from sqlite_orm.field import IntegerField, BooleanField, TextField
from sqlite_orm.table import BaseTable
from passlib.hash import pbkdf2_sha256
import ntplib
from time import ctime
import logging, os, settime

class Manage(BaseTable):
    __table_name__='users'
    #index, site_name, site_url,user_id, user_pw, date, content
    idx = IntegerField(primary_key=True, auto_increment=True)
    site_name = TextField(not_null=True)
    site_url = TextField()
    user_id = TextField(not_null=True)
    user_pw = TextField(not_null=True)
    content = TextField()
    date = TextField()

    def verify_login(self, _password):
        return pbkdf2_sha256.verify(_password, self.user_pw)

    def __repr__:
        return "user_id : %s" % user_id

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
    #select_user()
                        
    with Database("C:/Users/namki/Desktop/python_BasicProject/pm-python/shadow.db") as db:
        try:
            c = ntplib.NTPClient()
            response = c.request('europe.pool.ntp.org',version=3)
            print(ctime(response.tx_time)) #시간출력
        except ntplib.NTPException:
            print(ctime())
        
        #테이블 생성
        #db.query(Manage).create().execute()

        #데이터베이스 객체 생성
        #user1 = Manage(site_name="naver",site_url="www.naver.com",user_id="rltmd1004",user_pw="0000",content='',date=ctime(response.tx_time))
        
        #데이터베이스 객체 insert
        #db.query().insert(user1).execute()
        
        #select 출력문
        for row in db.query(Manage).select().execute():
            print(row)
        print(pbkdf2_sha256.hash("asd"))
