#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 1.py
@time: 2020/4/10  0:36
"""

class dog:
    list_dogs = [{'color': 'black', 'numbers': 100, 'price': 500},
                 {'color': 'white', 'numbers': 20, 'price': 800},
                 {'color': 'grey', 'numbers': 60, 'price': 700}]
    def sell(cls):
        type = input("购买黑色、白色、灰色请分别输入1、2、3:")
        cls.list_dogs[int(type)-1]['numbers'] -= 1

    def check(cls):
        for i in cls.list_dogs:
            print(i)

d = dog()
d.sell()
d.sell()
d.check()