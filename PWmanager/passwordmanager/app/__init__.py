#-*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for, session, json
from flask_sqlalchemy import SQLAlchemy
from views import *
from models import *
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config.from_object('config')
#app.secret_key="a"
app.register_blueprint(pw_program, url_prefix="/app")
#db = SQLAlchemy(app)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    