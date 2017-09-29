#!/usr/bin/env python
# coding=utf-8

import tornado.ioloop
import tornado.web
from hashlib import sha1
import os, time

# 将session以全局变量的形式保存
session_container = {}

# 创建cookie_str随机字符串  的函数
create_session_id = lambda: sha1('%s%s' % (os.urandom(16), time.time())).hexdigest()


class Session(object):
    # 静态字段--session key名
    session_id = "__sessionId__"

    def __init__(self, request):
        # 尝试获取__sessionId__
        session_value = request.get_cookie(Session.session_id)
        if not session_value:
            # 获取失败，就创建随机字符串
            self._id = create_session_id()
        else:
            # 成功---拿值
            self._id = session_value
        # 最后设置cookie---"__sessionId__:随机字符串"
        request.set_cookie(Session.session_id, self._id)

    def __getitem__(self, key):
        return session_container[self._id][key]

    def __setitem__(self, key, value):
        if session_container.has_key(self._id):
            session_container[self._id][key] = value
        else:
            session_container[self._id] = {key: value}

    def __delitem__(self, key):
        del session_container[self._id][key]


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        # my_session['k1']访问 __getitem__ 方法
        # 实例session对象，实现索引访问
        self.my_session = Session(self)


class MainHandler(BaseHandler):
    def get(self):
        print(self.my_session['c_user'])
        print(self.my_session['c_card'])
        self.write('index')


class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html', **{'status': ''})

    def post(self, *args, **kwargs):

        username = self.get_argument('name')
        password = self.get_argument('pwd')
        if username == 'wupeiqi' and password == '123':

            self.my_session['c_user'] = 'wupeiqi'
            self.my_session['c_card'] = '12312312309823012'

            self.redirect('/index')
        else:
            self.render('login.html', **{'status': '用户名或密码错误'})


settings = {
    'template_path': 'views',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh',
    'login_url': '/login'
}

application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/login", LoginHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()