#!/usr/bin/env python
# coding=utf-8

from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "shaoxia"

@app.route("/login")
def login():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>login</title>
</head>
<body>
<form action="">
    <input type="text" name="user">
    <input type="text" name="pwd">
    <input type="submit">
</form>
</body>
</html>
    '''

@app.route("/user/<name>")
def user(name):
    return name


app.run(debug=True)