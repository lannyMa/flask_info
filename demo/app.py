#!/usr/bin/env python
# coding=utf-8

from flask import Flask,render_template,request,flash
from models import User

app = Flask(__name__)
app.secret_key="123"


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginaction")
def loginaction():
    user = request.args.get("user")
    pwd = request.args.get("pwd")

    if not user:
        flash("pls input user")
        return render_template("login.html")
    if not pwd:
        flash("pls input pwd")
        return render_template("login.html")
    if user == "admin" and pwd == "123456":
        flash("welcome")
        return render_template("login.html")
    return render_template("login.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user")
def user_index():
    user = User("cristin","123345")
    return render_template("user.html",user = user)

app.run(debug=True)