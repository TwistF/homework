#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 8.py
@time: 2020/3/10  18:10
"""

#8  请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，
# 并打印出该字符及其出现的次数。
# 例如，输入 aaaabbc，输出：a:4


def max( str ):
    dict1 = {}
    for i in str:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    ans = sorted(dict1.items(), key = lambda x: x[1], reverse = True)
    print("%s:%d" %ans[0] )

# max("1131aaaa23123fffff")