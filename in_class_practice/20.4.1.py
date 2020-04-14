#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 20.4.1.py
@time: 2020/4/1  8:33
"""

def jia(a, b):
    return a+b

def jian(a, b):
    return a-b

def cheng(a, b):
    return a*b

def chu(a, b):
    if b == 0:
        return '除数不能为0'
    return a/b

def calcu(a, b, f):
    return f(a, b)

print(calcu(3, 2, jia))
print(calcu(2, 5, cheng))
print(calcu(3, 0, chu))