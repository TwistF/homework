#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 3.py
@time: 2020/3/10  16:01
"""

# 3 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；

list1 = list(range(1,100,2))
list2 = list(range(1,100,3))

for x in list1:
    if x in list2:
        print(x)