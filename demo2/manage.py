#!/usr/bin/env python
# coding=utf-8

import sqlite3
from flask_script import Manager
from app import app
from models import User
manager = Manager(app)

@manager.command
def hello():
    print "hello world"

@manager.option('-m','--msg',dest='msg_val',default="world")
def hello_world(msg_val):
    print "hello " + msg_val

@manager.command
def init_db():
    sql = "create table user (id INT, user TEXT)"
    conn = sqlite3.connect("user.db")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

@manager.command
def save():
    user = User(1,'jack')
    user.save()

@manager.command
def query_all():
    users = User.query()
    for user in users:
        print user


if __name__=="__main__":
    manager.run()