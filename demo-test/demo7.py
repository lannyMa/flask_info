#!/usr/bin/env python
# coding=utf-8

class DictDemo:
    def __init__(self, key, value):
        self.dict = {}
        self.dict[key] = value

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __len__(self):
        return len(self.dict)

    @staticmethod
    def show(self):
        print "oh, i am ..."


dd = DictDemo('lanny','1995')
dd['show']

#
# dictDemo = DictDemo('key0', 'value0')
# print(dictDemo['key0'])  # value0
# dictDemo['key1'] = 'value1'
# print(dictDemo['key1'])  # value1
# print(len(dictDemo))  # 2
#
