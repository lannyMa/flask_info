#!/usr/bin/env python
# coding=utf-8

from flask import Flask,render_template
import pymysql

conn =pymysql.connect(host='127.0.0.1',user='root',password = '',database='bbs')

conn.autocommit(True)
cur = conn.cursor()
# cur.execute("insert into users VALUES ('cristin','1995');")
conn.commit()
cur.execute("select * from users;")
print cur.fetchall()

app = Flask(__name__)

@app.route("/")
def index():
    cur.execute("select * from users;")
    return render_template("index.html", user_list = cur.fetchall())

app.run(debug=True)