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

    def __repr__():
        return "user_id : %s" % user_id

def insert_user(__site_name, __site_url, __user_id, __user_pw, __content=''):
    with Database(os.getcwd().replace("\\","/")+"/shadow.db") as db:
        #데이터베이스 객체 생성
            objectname = __site_name
            objectname = Manage(site_name=__site_name,site_url=__site_url,user_id=__user_id,user_pw=__user_pw,content=__content,date=settime.get_time())
        #데이터베이스 객체 insert
            db.query().insert(objectname).execute()
    pass

def select_user(input_id=''):
    row_fetch=list()
    with Database(os.getcwd().replace("\\","/")+"/shadow.db") as db:
    #select 출력문        
        for row in db.query(Manage).select().execute():            
            row_fetch.append(row)
        #print(pbkdf2_sha256.hash("asd"))
    return row_fetch

def select_user_pw(input_name):
    row_fetch=list()
    with Database(os.getcwd().replace("\\","/")+"/shadow.db") as db:       
        res = db.query(Manage).filter(Manage.site_name == input_name).select().execute().fetchone()
    return res

def delete_site(input_num):
    with Database(os.getcwd().replace("\\","/")+"/shadow.db") as db:       
        db.query(Manage).filter(Manage.idx == int(input_num)).delete().execute()
    pass

def create_db():
    with Database(os.getcwd().replace("\\","/")+"/shadow.db") as db:
    #테이블 생성
        user = db.query(Manage).create().execute()
    pass
def update_info(input_name):
    with Database(os.getcwd().replace("\\","/")+"/shadow.db") as db:
        _user = db.query(Manage).filter(Manage.site_name == input_name).select().execute().fetchone()
        print("[1] Site idx : %s" % (_user[0])) #idx
        print("[2] Site name : %s" % (_user[1])) #site_name
        print("[3] Site url : %s" % (_user[2])) # site_url
        print("[4] Site id : %s" % (_user[3])) # user_id
        print("[5] Site pw : %s" % (_user[4])) # user_pw
        update_type = input(">>")
        if update_type == str(2): #hostname
            _hostname = input("new hostname : ")
            pass
        elif update_type == str(3): #hosturl
            _url = input("new host url : ")
            pass
        elif update_type == str(4):#ID
            _ID = input("new ID : ")
            pass
        elif update_type == str(5):#PW
            _Password = input("new Password : ")
            pass
        else:
            pass  
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
