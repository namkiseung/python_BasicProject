from sqlite_orm.database import Database
from sqlite_orm.field import IntegerField, BooleanField, TextField
from sqlite_orm.table import BaseTable
from passlib.hash import pbkdf2_sha256
import ntplib
from time import ctime
import logging

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

if __name__=="__main__":
    #logger configure:
    logging.basicConfig(filename="C:/Users/namki/Desktop/python_BasicProject/pm-python/error.log", level=logging.DEBUG, format=('%(asctime)s: '
                                                                            '%(filename)s: '
                                                                            '%(levelname)s: '
                                                                            '%(funcName)s(): '
                                                                            '%(lineno)d: '
                                                                            '%(message)s'), datefmt="%Y-%m-%d %H:%M:%S")
                        
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
