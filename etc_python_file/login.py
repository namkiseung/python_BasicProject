# -*- coding:utf-8 -*-
import sqlite3
from passlib.hash import pbkdf2_sha256

#db = sqlite3.connect("test.db")

while True:
   _id = raw_input("ID: ")
   _pw = raw_input("PW: ")
   
   if _id == "rltmd1004":
      print "[*] success"
      print pbkdf2_sha256.hash(_pw)
      break
   else:
      print "[!] failed"
      print pbkdf2_sha256.hash(_pw)
    
