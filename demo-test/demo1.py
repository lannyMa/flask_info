#!/usr/bin/env python
# coding=utf-8

def outer(func):
    def inner():
        print "hello"
        print "hello"
        print "hello"
        r = func()
        print "world"
        print "world"
        return r
    return inner

# @outer
def f1():
    print "hahahaa"

f1=outer(f1)
f1()