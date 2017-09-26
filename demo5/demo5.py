#!/usr/bin/env python
# coding=utf-8


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    user = "123"
    return render_template("user.html", user=user)


@app.route("/login")
def login():
    user = request.args.get("user",None)
    return render_template("user.html", user=user)


@app.route("/login2/<user>")
def login2(user):
    return render_template("user.html", user=user)


@app.route("/list")
def txl_show():
    names = ["jack","cristin","bob"]
    return render_template("txl_show.html",names = names)


app.run(debug=True)
