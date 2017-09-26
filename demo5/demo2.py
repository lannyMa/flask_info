#!/usr/bin/env python
# coding=utf-8


from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    ua = request.headers.get("User-Agent")
    al = request.headers.get("Accept-Language","oh no!")
    rurl = request.headers.get("Request URL","oh no!")
    ck = request.headers.get("Cookie","oh no!")
    return ck



app.run(debug=True)