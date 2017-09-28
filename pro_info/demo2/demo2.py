#!/usr/bin/env python
# coding=utf-8

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    Cookie = request.headers.get("Cookie")
    return "<h1>Your brower is</h1>  %s<br> %s" % (user_agent,Cookie)

@app.route("/login")
def login():
    return "welcome to login"

app.run(debug=True)
