#!/usr/bin/env python
# coding=utf-8

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html",err_msg = "")

@app.route("/loginaction")
def login():
    err_msg=""
    user = request.args.get("user")
    pwd = request.args.get("pwd")
    if user == "admin" and pwd == "123456":
        err_msg = "logging successful"
    else:
        err_msg = "user or pwd error"
    return render_template("login.html",err_msg=err_msg)

app.run(debug=True)