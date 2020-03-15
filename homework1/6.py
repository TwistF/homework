#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 6.py
@time: 2020/3/10  16:33
"""

# 6  前面2个元素为0，1，输出100以内的斐波那契数列；

def fib( a ):
    if a == 0:
        return 0;
    if a == 1:
        return 1;
    return fib(a-1) + fib(a-2)

for i in range(100) :
    x3 = fib(i)
    if( x3 > 100):
        break
    print(x3)