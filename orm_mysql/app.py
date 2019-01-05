
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template, Flask, redirect, url_for
from mysql_control import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"

db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/chk", methods=['POST'])
def index2():
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
        return '''<h1>userid : %s, userpw : %s </h1> <button onlick='javascript:history.go(-1);'>뒤로가기</button> '''%(userid, userpw)
    #틀리면 뒤로
    return redirect(url_for('index'))

if __name__=="__main__":
    #db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)