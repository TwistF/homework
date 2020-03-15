#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 5.py
@time: 2020/3/10  16:07
"""

#5  使用random模块，生成随机数，来初始化一个列表，元组；
#     使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；

import random

list1 = []
list2 = []

for x in range(10):
    list1.append(random.randint(1,100))
    list2.append(random.randint(1,100))

print(list1)
print(tuple(list2))