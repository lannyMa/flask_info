#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html.html")


@app.route("/login")
def login():
    return render_template("login.html", name="maotai")



@app.route("/login2/<name>")
def login2(name):
    # return name
    return render_template("login.html",name=name)

@app.route("/test")
def emy():
    names = ["jack","<h1>linken words</h1>"," cristin "]
    info = {
        "jack":22,
        "cristin":18,
    }
    # return render_template("test.html",names = names)
    return render_template("test.html",names = names, info = info)



app.run(debug=True)
