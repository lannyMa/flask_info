#!/usr/bin/env python
# coding=utf-8

def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]

    return incr


count = counter(10)
print(count())
print(count())
print(count())
print(count())