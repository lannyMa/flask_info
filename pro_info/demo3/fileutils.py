#!/usr/bin/env python
# coding=utf-8

file_dict = {}
# file => dict

def read_file():
    with open("users.txt") as f:
        for line in f.readlines():
            user,pwd = line.split()
            file_dict[user]=pwd
    return file_dict

# dict => file
def write_file():
    tmp=[]
    for user,pwd in file_dict.items():
        tmp.append("%s %s"%(user,pwd))
    with open("users.txt","w") as f:
        f.write("\n".join(tmp))



