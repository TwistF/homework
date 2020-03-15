#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 7.py
@time: 2020/3/10  16:40
"""

# 7 打印输出9*9乘法表

for i in range(1,10):
    for j in range(1, i+1):
        print("%dx%d=%d"%(j, i, i*j), end = '')
        print("    ", end = '')
    print('')
