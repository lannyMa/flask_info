#!/usr/bin/env python
# coding=utf-8

from __future__ import unicode_literals
import feedparser
from flask import Flask

ZHIHU_FEED = "https://www.zhihu.com/rss"

app = Flask(__name__)


@app.route("/")
def index():
    feed = feedparser.parse(ZHIHU_FEED)
    first_content = feed["entries"][0]
    http_format = """
        <html>
        <head><meta charset="UTF-8"></head>
        <body>
            <h1>zhihu news</h1>
            <b>{0}</b><br>
            <b>{1}</b><br>
            <b>{2}</b><br>
        </body>
        </html>
    """
    return http_format.format(first_content.get('title'),
                            first_content.get("published"),
                            first_content.get("summary")
                            )

app.run(debug=True)