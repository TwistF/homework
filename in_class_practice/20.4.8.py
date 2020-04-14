#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 20.4.8.py
@time: 2020/4/8  9:12
"""

class dog:
    number = 0
    name = ''
    color = ''

    def __init__(self, n, c):
        self.name = n
        self.color = c

    def woof(self):
        print("%s is woofing"%self.name)

    @classmethod
    def add(cls):
        cls.number += 1

dog1 = dog('a', 'white')
dog.add()
dog2 = dog('b', 'brown')
dog.add()

dog1.woof()
dog2.woof()

print(dog.number)