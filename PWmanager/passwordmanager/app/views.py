#-*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for, session, json, Blueprint
from flask_sqlalchemy import SQLAlchemy
#from app import views
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key="a"
pw_program = Blueprint('page', __name__,
                        template_folder='templates')
@pw_program.route("/", methods=['GET', 'POST'])
def index():
    #세션없으면 로그인페이지 이동시키기
    if session.get('login') == False:
        return redirect(url_for('loginpage'))
    
    #사용자의 사이트 정보를 DB 에서 가져온다
    sitelist = Site_info.query.all()
    return render_template('index.html', sitelist = sitelist)

@pw_program.route("/login", methods=['GET', 'POST'])
def loginpage():
    return render_template('login.html')

@pw_program.route("/login_chk", methods=['POST'])
def index2():
    userid = request.form.get("id")
    userpw = request.form.get("pw")
    #백도어
    if userid=="root":
        session['login'] = True
        return redirect(url_for("index"))
    try:
        #ORM에 의해 로그인 사용자 확인하는 구간
        q1 = Site_info.query.filter(Site_info.userid==userid).first()
        q2 = Site_info.query.filter(Site_info.userpw==userpw).first()
    except:
        pass
    #아디와 비번값이 DB에 있으면 로그인됨.    
    if q1 is None or q2 is None:
        return redirect(url_for("loginpage"))
    else:
        session['login'] = True
        return redirect(url_for("index"))

@pw_program.route("/logout", methods=['GET'])
def logout():
    session.pop('login')
    return redirect(url_for('loginpage'))

@pw_program.route("/view_route/<sitename>/<_userid>", methods=['GET'])
def view_route(sitename, _userid):
    #print("sitename : {}, userid : {}".format(sitename, _userid))
    #Ajax에서온 sitename의 싸이트가 있는지 확인(DB에서)
    chk_site=Site_info.query.filter(Site_info.sitename==sitename).first()
    #데이터 있으면
    if chk_site is not None:
        #배열에서 userid를 찾아 입력받은 id가 있는지 확인하기
        chk_userid=Site_info.query.filter(Site_info.userid==_userid).first()
        #데이터 있으면
        if chk_userid is not None:
            return json.dumps(["ID : {}".format(chk_userid.userid), "PW : {}".format(chk_userid.userpw)])
            #json dumps로 계정과 패스워드 리턴하기
        #데이터 없으면
            #"계정이 존재하지 않습니다" 출력
    #데이터 없으면
        #"해당 사이트가 존재하지 않습니다" 출력
    pass

@pw_program.route("/add_info", methods=['GET', 'POST'])
def add_info():
    if request.method == 'GET':
        return render_template("add_info.html")
    elif request.method == 'POST':
        #form 데이터 다 가져오기
        _sitename=request.form.get('sitename')
        _siteurl=request.form.get('siteurl')
        _userid=request.form.get('userid')
        _userpw=request.form.get('userpw')
        _snsauth=request.form.get('snsauth')
        user_add(sitename=_sitename, snsauth=_snsauth, url=_siteurl, userid=_userid, userpw=_userpw)
        return redirect(url_for("index"))
    pass

@pw_program.route("/update_info/<num>", methods=['GET', 'POST'])
@pw_program.route("/update_info", methods=['GET', 'POST'])
def update_info(num=''):
    if request.method == 'GET':
        q1 = Site_info.query.filter(Site_info.idx==num).first()
        return render_template("update_info.html", datas=q1)
    elif request.method == 'POST':
        #form 데이터 다 가져오기
        _sitename=request.form.get('sitename')
        _siteurl=request.form.get('siteurl')
        _userid=request.form.get('userid')
        _userpw=request.form.get('userpw')
        _snsauth=request.form.get('snsauth')
        user_update(sitename=_sitename, snsauth=_snsauth, url=_siteurl, userid=_userid, userpw=_userpw)
        return redirect(url_for("index"))

@pw_program.route("/del", methods=['GET'])
def del_site():
    user_del(request.args.get("sitename"))
    return redirect(url_for("index"))