#!/usr/bin/env python
# coding=utf-8


from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def user():
    return render_template("index.html.html",name="jacks")



@app.route("/list")
def names():
    names = ['lanny','jack','maotai']
    return render_template("index.html.html",names = names)


app.run(debug=True)