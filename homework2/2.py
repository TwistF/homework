#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 2.py
@time: 2020/3/10  17:22
"""

# 2 编写一个函数,接收n个数字，求这些参数数字的和;

def sum( *args ):
    x = 0
    for i in args:
        x += i
    return x

# print(sum(1,2,3,4)) 测试用