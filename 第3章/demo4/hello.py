#!/usr/bin/env python
# coding=utf-8

from flask import session, redirect, url_for, flash, render_template, Flask
from flask.ext.bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    flash('hi maotai!!!')
    flash('hi maotai!!!')
    flash('hi maotai!!!')
    flash('hi maotai!!!')
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',
                           form=form, name=session.get('name'))

app.run(debug=True)
