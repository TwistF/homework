#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 4.py
@time: 2020/3/10  17:27
"""

# 4  写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;

def count( a ):
    dict1 = {"letters": 0, "numbers": 0, "space": 0, "others": 0}
    for i in a:
        if i.isalpha():
            dict1["letters"] += 1
        elif i.isdigit():
            dict1["numbers"] += 1
        elif i == " ":
            dict1["space"] +=1
        else:
            dict1["others"] += 1
    print(dict1)

# count("i can because 1213...")
