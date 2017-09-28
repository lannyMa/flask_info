#!/usr/bin/env python
# coding=utf-8

from flask import Flask, request, render_template,redirect,session
import fileutils


import MySQLdb as mysql

conn = mysql.connect(host="127.0.0.1",user="root",passwd="",db="bbs")
cur = conn.cursor()
cur.execute("select * from users;")
print cur.fetchall()

# conn.autocommit(True)


fileutils.read_file()

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yXasdfasdfadsfsd3243432432432R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
    if "username" in session:
        return redirect("/list")
    else:
        return render_template("login.html", err_msg="")


@app.route("/loginaction")
def loginaction():
    err_msg = ""
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    if user == "admin" and pwd == "123456":
        session['username']="admin"
        return redirect("/list")
    else:
        err_msg = "user or pwd error"
    return render_template("login.html", err_msg=err_msg)


@app.route("/list")
def user_list():
    cur.execute("select * from users;")
    if "username" in session:
        return render_template("list.html",user_list=cur.fetchall())
    else:
        return redirect("/")


@app.route("/del")
def delete_user():
    user = request.args.get("user")
    cur.execute("delete from users where user ='%s'"%user)
    conn.commit()
    return redirect("/list")


@app.route("/adduser")
def add_user():
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    cur.execute("select user from users")
    flag = 0
    for tmp_user in cur.fetchall():
        if user == tmp_user[0]:
            flag=1
        else:
            flag=0
    if flag==1:
        return redirect("/list")
    else:
        cur.execute("insert into users values ('%s','%s')"%(user,pwd))
        conn.commit()
        return redirect("/list")



@app.route("/update")
def update_user():
    user = request.args.get("user")
    cur.execute("select pwd from users where user='%s'"%user)
    pwd = cur.fetchall()
    return render_template("update.html",user=user,pwd=pwd[0][0])

@app.route("/updateaction")
def update_action():
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    cur.execute("update users set pwd='%s' where user='%s';"%(pwd,user))
    conn.commit()
    # fileutils.file_dict[user]=pwd
    return redirect("/list")


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect("/")



@app.route("/login",methods=["GET","POST"])
def login():
    print request.method
    if request.method=="GET":
        return render_template("login.html", err_msg="")
    elif request.method=="POST":
        user=request.form.get("user")
        pwd=request.form.get("pwd")




app.run(debug=True)
