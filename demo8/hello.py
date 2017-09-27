#!/usr/bin/env python
# coding=utf-8

from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template("base.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404


@app.route("/user/<name>")
def show_user(name):
    return render_template("user.html",name=name)

app.run(debug=True)