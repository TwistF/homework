#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 6.py
@time: 2020/3/10  17:59
"""

# 6  定义一个函数, 打印输出n以内的斐波那契数列;

def fib( n ):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_plus( n ):
    i = 1;
    while True:
        cur = fib(i)
        if cur > n:
            break
        print(cur)
        i += 1

# fib_plus(1000)