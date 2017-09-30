#!/usr/bin/env python
# coding=utf-8

import MySQLdb as ms

class DB:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.connect()

    def connect(self):
        self.conn = ms.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            db=self.db
        )
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            self.cursor.close()
            self.conn.close()
            self.connect()
            return self.execute(sql)
        else:
            return self.cursor

    # def query(self,tables):
    #     sql = 'select * from users'
    #     self.cursor.execute(sql)
    #     return self.cursor.fetchall()
