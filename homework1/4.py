#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 4.py
@time: 2020/3/10  16:03
"""

# 4  判断用户输入的年份是否为闰年

year = int(input("year:"))

if year%4 == 0 and ( year%100 !=0 or year%400 == 0):
    print("是闰年")
else:
    print("不是闰年")