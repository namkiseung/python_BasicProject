#-*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for, session, json
from flask_sqlalchemy import SQLAlchemy
#from app import views
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key="a"
db = SQLAlchemy(app)

def get_day():
    d = datetime.date.today()
    return d.ctime()

class Site_info(db.Model):
    __tablename__ = 'site_info'
    idx = db.Column(db.Integer, primary_key=True)
    sitename = db.Column(db.String(30))
    snsauth = db.Column(db.String(10))
    url = db.Column(db.String(500))
    userid = db.Column(db.String(100))
    userpw = db.Column(db.String(150))
    rdate = db.Column(db.String(30))

    def __init__(self, sitename='', snsauth='', url='', userid='', userpw=''):
        self.sitename = sitename
        self.snsauth = snsauth
        self.url = url
        self.userid = userid
        self.userpw = userpw
        self.rdate = get_day()

    def __repr__(self):
        return "<idx:%d, sitename:%s, snsauth:%s, url:%s, userid:%s, userpw:%s, rdate:%s>" % (
            self.idx, self.sitename, self.snsauth, self.url, self.userid, self.userpw, self.rdate)

def user_add(sitename='', snsauth='', url='', userid='', userpw=''):
    obj_ms = Site_info(sitename, snsauth, url, userid, userpw)
    db.session.add(obj_ms)
    db.session.commit()
    pass
def user_update(sitename='', snsauth='', url='', userid='', userpw=''):
    obj_ms = Site_info.query.filter(Site_info.userid == userid).first()
    obj_ms.sitename = sitename
    obj_ms.snsauth = snsauth
    obj_ms.url = url
    obj_ms.userid = userid
    obj_ms.userpw = userpw
    db.session.add(obj_ms)
    db.session.commit()
    pass
def user_del(sitename):
    obj_ms = Site_info.query.filter(Site_info.sitename == sitename).first()
    db.session.delete(obj_ms)
    db.session.commit()
    pass
