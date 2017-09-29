#!/usr/bin/env python
# coding=utf-8


class A:
    def bar(self):
        print "a bar"


class B():
    pass

class C(A):
    pass

class D():
    pass

d = D()
d.bar()