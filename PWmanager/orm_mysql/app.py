
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template, Flask, redirect, url_for, session, json
from mysql_control import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"
app.secret_key="fun"
db = SQLAlchemy(app)

@app.route("/index/check/<num>/<username>") #'보기'버튼 클릭시 ID를 체크할때
def index_check(num, username):
    session_chk()
    namki = Site_info.query.filter(Site_info.idx == num).first()
    if namki is not None:
        return redirect(url_for('index_view', username=username))
    return redirect(url_for('index'))

@app.route("/index/view/<username>") #'보기'버튼 클릭시 ID체크 후에 계정 내용보이기
def index_view(username):
    name=Site_info.query.filter(Site_info.userid == username).first()
    print(name)
    render = render_template('view.html', info=name)
    response=list()
    response.append(render)
    return json.dumps(response).encode('utf-8')

@app.route("/update/check/<num>") #'수정'버튼 클릭시 ID체크
@app.route("/update/view/<num>") #'수정'버튼 클릭시 ID체크 후에 계정 내용보이기(input type=text)
@app.route("/update/modify/<num>") #'수정'버튼 클릭시 ID체크 후에 계정 내용수정된 상태에서 제출버튼 눌렀을 때

@app.route("/delete/check/<num>") #'삭제' 버튼 클릭시 site이름 입력받는다.
@app.route("/delete/<num>") #'삭제' 버튼 클릭시 site이름 입력받고 맞으면 삭제

def session_chk():
    if session.get('login') is not True:
        return redirect(url_for('login'))
    pass #return redirect(url_for('index'))

@app.route("/", methods=['GET'])
@app.route("/<nickname>", methods=['GET'])
def index(nickname=''):
    session_chk() #check the session function
    #Select 문으로 site name모조리 뽑아오자
    site_info = Site_info.query.all()
    return render_template('mainlist.html', site_info=site_info, login_chk=session.get('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route("/chk", methods=['POST'])
def login_chk():
    userid=request.form.get("id")
    userpw=request.form.get("pw")
    print(userid)
    print(userpw)
    qry1=Site_info.query.filter(Site_info.userid==userid)
    qry2=Site_info.query.filter(Site_info.userpw==userpw)
    res=qry1.first()
    res2=qry2.first()
    print("id : {}".format(res))
    print("pw : {}".format(res2))
    #print("출력은 : {}, {}".format(res.userid, res.userpw))
    #아이디가 뽑아온게   맞으면 
    if res is not None:# or res2 is not None:
        session['login'] = True #로그인 확인
        return redirect(url_for('index', userid=userid))#'''<h1>userid : %s, userpw : %s </h1> <button onlick='javascript:history.go(-1);'>뒤로가기</button> '''%(userid, userpw)
    #틀리면 뒤로
    return redirect(url_for('login'))

if __name__=="__main__":
    #db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)