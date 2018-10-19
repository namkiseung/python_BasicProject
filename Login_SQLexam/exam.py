# -*- coding:utf-8 -*-
import sqlite3

db = sqlite3.connect("test.db")

while True:
   _id = raw_input("ID: ")
   _pw = raw_input("PW: ")
   sql_string = "SELECT * FROM users WHERE id='{}' and pw='{}'".format(_id, _pw)

   print sql_string
   cur = db.execute(sql_string)
   result = cur.fetchall()

   if result:
      print "[*] success"
      print "\t", result
   else:
      print "[!] failed"

   #db.execute("CREATE TABLE users(id text, pw text)")
#db.execute("INSERT INTO users VALUES ('rltmd', '1234')")
   #db.commit()
   #db.close()
