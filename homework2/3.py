#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 3.py
@time: 2020/3/10  17:24
"""

#3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#   数字列表请用随机数函数生成;

import random

def odd( a ):
    for i in a:
        if i % 2 == 1:
            print(i)

list1 = []
for i in range(10):
    list1.append(random.randint(0,9))

odd(list1)