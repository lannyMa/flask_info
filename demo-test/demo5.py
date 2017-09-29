#!/usr/bin/env python
# coding=utf-8

class Fu(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    @staticmethod
    def query2():
        info = [
            (1, 'aaron'),
            (2, 'boby'),
            (3, 'cristin'),
        ]
        users = []
        for user in info:
            tmp = Fu(user[0],user[1])
            users.append(tmp)
        return users

    def __str__(self):
        return 'id:{}--name:{}'.format(self.id, self.name)


print Fu.query2()
users = Fu.query2()
for line in users:
    print line
