#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template, request, redirect, flash, session,url_for
import fileutils
import MySQLdb as mysql

conn = mysql.connect(host='127.0.0.1',user='root',passwd='',db='bbs')
cur = conn.cursor()
sql = "select * from users"
cur.execute(sql)
conn.autocommit(True)
print cur.fetchall()

app = Flask(__name__)
app.secret_key = "1992"


@app.route("/")
def login():
    if "username" in session:
        return redirect("/list")
    else:
        return render_template("login.html")

@app.route("/loginaction")
def login_action():
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    cur.execute("select * from users")
    for line in cur.fetchall():
        suser,spwd = line
        print suser,spwd
        if suser == user and spwd == pwd:
            session['username']=user
            return redirect("/list")

    flash("user or pwd is error")
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect("/")

@app.route("/list")
def show_user():
    cur.execute("select * from users")
    if "username" in session:
        user_list = fileutils.read_file()
        return render_template("list.html", user_list=cur.fetchall())
    else:
        return redirect("/")

@app.route("/adduser")
def add_user():
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    if user and pwd:
        cur.execute("select * from users")
        for line in cur.fetchall():
            suser,spwd = line
            if suser == user:
                return redirect("/list")
        else:
            cur.execute("insert into users values('%s','%s')"%(user,pwd))
            return redirect("/list")
    else:
        return redirect("/list")


@app.route("/del")
def del_user():
    user = request.args.get("user")
    cur.execute("delete from users where user ='%s';"% user)
    return redirect("/list")


@app.route("/update")
def update_user():
    user = request.args.get("user")
    cur.execute("select pwd from users where user='%s'"%user)
    pwd = cur.fetchall()[0][0]
    return render_template("update.html", user=user, pwd=pwd)


@app.route("/updateaction")
def update_action():
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    print user, pwd
    cur.execute("update users set pwd='%s' where user = '%s'" % (pwd,user))
    return redirect("/list")

app.run(debug=True)
