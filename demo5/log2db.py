#!/usr/bin/env python
# coding=utf-8

from dbutils import DB

db = DB(
    host="127.0.0.1",
    user="root",
    passwd="",
    db="logtest"
)

res = {}

with open('log.txt') as f:
    for line in f:
        if line == "\n":
            continue
        arr = line.split(" ")
        ip = arr[0]
        status = arr[8]
        res[(ip, status)] = res.get((ip, status), 0) + 1

for l in sorted(res.items(),key=lambda x:x[1],reverse=True):
    sql = "insert into log values ('%s','%s','%s')"%(l[0][0],l[0][1],l[1])
    db.execute(sql)
