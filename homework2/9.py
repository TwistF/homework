#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 9.py
@time: 2020/3/10  18:15
"""

# 9  定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序
# (冒泡排序,  也可以直接使用相关的函数);

def st ( number ):
    number.sort()
    return number

print(st([5,2,3,4]))