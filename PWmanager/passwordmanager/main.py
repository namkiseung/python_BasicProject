#-*- coding: utf-8 -*-
from app import __init__
from app.views import pw_program
from flask import Flask
app = Flask(__name__)
app.register_blueprint(pw_program, url_prefix="/app")
print(app)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    