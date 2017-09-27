#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(Form):
    name = StringField("what is your name? ", validators=[Required()])
    submit = SubmitField('submit')


@app.route("/", methods=['GET', 'POST'])
def index():
    name_value = None
    form = NameForm()
    if form.validate_on_submit():
        # 保存的是表单里的值
        name_value = form.name.data
        form.name.data = ""
    return render_template("index.html", form=form, name=name_value)


app.run(debug=True)
