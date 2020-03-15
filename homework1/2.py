#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 2.py
@time: 2020/3/10  15:47
"""

# 2 一个字典中，存放了10个学生的学号（key）和分数（value）；
# 请筛选输出，大于80分的同学（按照格式：学号：分数）；

dict = [{'key': 120, 'value': 90},
        {'key': 121, 'value': 70},
        {'key': 123, 'value': 74},
        {'key': 125, 'value': 92},
        {'key': 126, 'value': 100},
        {'key': 127, 'value': 80},
        {'key': 129, 'value': 90},
        {'key': 200, 'value': 83},
        {'key': 208, 'value': 85},
        {'key': 210, 'value': 90},]

for x in dict:
    if x['value'] > 80:
        print(x['key'], ": ", x['value'])