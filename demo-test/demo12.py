#!/usr/bin/env python
# coding=utf-8



class Fu:
    def __init__(self):
        print("fu init")
        self.ty="mao"


class Zi(Fu):
    def __init__(self):
        # 方法1 不推荐
          # super(Zi, self).__init__()
        # 方法2: 推荐
        Fu.__init__(self)
        print("zi init")


z = Zi()