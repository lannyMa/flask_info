#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template, request, redirect, flash, session,url_for

import fileutils

app = Flask(__name__)
app.secret_key = "1992"

@app.route("/head")
def get_header():
    user_agent = request.headers.get("User-Agent")
    Cookie = request.headers.get("Cookie")
    return "{{ session.username }}------- %s"%Cookie

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
    fileutils.read_file()
    if fileutils.file_dict.has_key(user) and pwd == fileutils.file_dict[user]:
        session['username'] = user
        session['password'] = pwd
        return redirect("/list")
    else:
        flash("user or pwd is error")
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect("/")

@app.route("/list")
def show_user():
    print session
    if "username" in session:
        user_list = fileutils.read_file()
        return render_template("list.html", user_list=user_list.items())
    else:
        return redirect("/")

@app.route("/adduser")
def add_user():
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    fileutils.read_file()
    if user in fileutils.file_dict:
        return redirect("/list")
    else:
        fileutils.file_dict[user] = pwd
        fileutils.write_file()
        return redirect("/list")


@app.route("/del")
def del_user():
    user = request.args.get("user")
    fileutils.read_file()
    fileutils.file_dict.pop(user)
    fileutils.write_file()
    return redirect("/list")


@app.route("/update")
def update_user():
    user = request.args.get("user")
    fileutils.read_file()
    pwd = fileutils.file_dict[user]
    return render_template("update.html", user=user, pwd=pwd)


@app.route("/updateaction")
def update_action():
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    print user, pwd
    fileutils.read_file()
    print fileutils.file_dict
    fileutils.file_dict[user] = pwd
    print fileutils.file_dict
    fileutils.write_file()
    return redirect("/list")

app.run(debug=True)
