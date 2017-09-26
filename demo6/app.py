#!/usr/bin/env python
# coding=utf-8

from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html.html")

app.run(debug=True)