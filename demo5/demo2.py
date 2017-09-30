#!/usr/bin/env python
# coding=utf-8


info = {
    'lanny': 1992,
    'jack': 1994,
    'emy': 1984,
    'cristin': 1912,
}

s = info.items()
print s                                             # [('lanny', 1992), ('emy', 1984), ('jack', 1994), ('cristin', 1912)]
print sorted(s,key=lambda x:x[1])                  # 默认从小到大排列,[('cristin', 1912), ('emy', 1984), ('lanny', 1992), ('jack', 1994)]
print sorted(s,key=lambda x:x[1],reverse=True)     # 从大到小排列