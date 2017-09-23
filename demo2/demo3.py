#!/usr/bin/env python
# coding=utf-8


from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def user():
    return render_template("index.html",name="jacks")

app.run(debug=True)