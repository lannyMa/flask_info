#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
    name = StringField("what is your name? ")
    submit = SubmitField('submit')

@app.route("/")
def index():
    form = NameForm()
    return render_template("index.html", form=form)

app.run(debug=True)
