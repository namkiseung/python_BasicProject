# -*- coding: utf-8 -*-
import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"

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
       return "idx:{}, sitename: {}, snsauth:{}, url: {}, userid: {}, userpw: {}, rdate: {}".format(
           self.idx, self.sitename, self.snsauth, self.url, self.userid, self.userpw, self.rdate)

def user_add(sitename='', snsauth='', url='', userid='', userpw=''):
    namki = Site_info(sitename, snsauth, url, userid, userpw)
    db.session.add(namki)
    db.session.commit()

def user_del(index):
    pass





if __name__=="__main__":
    #db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
    
    
