#!/usr/bin/env python
# coding=utf-8

from flask import Flask, request, render_template,redirect,session
import fileutils


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
def login():
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
    if "username" in session:
        return render_template("list.html",user_list=fileutils.file_dict.items())
    else:
        return redirect("/")


@app.route("/del")
def delete_user():
    user = request.args.get("user")
    fileutils.file_dict.pop(user)
    fileutils.write_file()
    return redirect("/list")


@app.route("/adduser")
def add_user():
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    if user in fileutils.file_dict:
        return redirect("/list")
    else:
        fileutils.file_dict[user]=pwd
        fileutils.write_file()
        return redirect("/list")


@app.route("/update")
def update_user():
    user = request.args.get("user")
    pwd = fileutils.file_dict[user]
    return render_template("update.html",user=user,pwd=pwd)

@app.route("/updateaction")
def update_action():
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    fileutils.file_dict[user]=pwd
    return redirect("/list")


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect("/")

app.run(debug=True)
