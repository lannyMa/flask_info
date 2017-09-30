#!/usr/bin/env python
# coding=utf-8

import json

from flask import Flask, render_template
from dbutils import DB

db = DB(
    host="127.0.0.1",
    user="root",
    passwd="",
    db="logtest"
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("echarts-pie.html")


@app.route("/piedata")
def piedata():
    sql = "select status,sum(count) from log group by status";
    # res = db.execute(sql)
    # print res.fetchall()
    cur =  db.execute(sql)
    res = {
        'legend':[],
        'data':[]
    }
    # for c in cur.fetchall():
    #     code = c[0]
    #     count = c[1]
    #     print code,count
    # return "pie"
    for c in cur.fetchall():
        code = c[0]
        count = int(c[1])
        res['legend'].append(code)
        res['data'].append({
            'name': code,
            'value': count
        })
    return json.dumps(res)
app.run(debug=True)
