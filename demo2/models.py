#!/usr/bin/env python
# coding=utf-8
import sqlite3
def get_conn():
    return sqlite3.connect("user.db")

class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def save(self):
        sql = 'insert into user VALUES (?,?)'
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql, (self.id, self.name))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def query():
        sql = 'select * from user'
        conn = get_conn()
        cur = conn.cursor()
        rows = cur.execute(sql)
        users = []
        for row in rows:
            print row,type(row)
            user = User(row[0], row[1])
            users.append(user)
            print users,type(users)

        conn.commit()
        cur.close()
        conn.close()
        return users

    def __str__(self):
        return 'id:{}--name:{}'.format(self.id, self.name)

users = User.query()
for user in users:
    print user
