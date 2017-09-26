#!/usr/bin/env python
# coding=utf-8

from flask import Flask

app = Flask(__name__)

@app.route("/<a>/<b>")
def index(a,b):
    c = int(a)+int(b)
    return str()

app.run(debug=True)