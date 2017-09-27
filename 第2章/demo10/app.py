#!/usr/bin/env python
# coding=utf-8


from flask import Flask,render_template
from flask.ext.moment import Moment
from datetime import datetime


app = Flask(__name__)
moment = Moment(app)
@app.route("/")
def index():
    return render_template("base.html",current_time=datetime.utcnow())




app.run(debug=True)


