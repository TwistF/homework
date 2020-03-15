#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 10.py
@time: 2020/3/10  18:20
"""

# 10 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)

def caculate( str ):
    for i in range(len(str)):
        if str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
            break
    a = float( str[:i] )
    b = float( str[i+1:] )
    if str[i] == '+':
        return a+b
    if str[i] == '-':
        return a-b
    if str[i] == '*':
        return a*b
    if str[i] == '/':
        return a/b

print(caculate("1.3+4.5"))