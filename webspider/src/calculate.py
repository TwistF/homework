#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: calculate.py
@time: 2020/6/16  20:04
"""

import re
from src import db_connect

def ans():

    connections = db_connect.connect()
    sal_list = db_connect.read_salaries(connections[1], connections[0])

    count = 0
    total = 0

    for i in sal_list:
        # print(i[0])
        value_list = re.findall(r"\d+\.?\d*",i[0])
        value = 0
        if len(value_list) == 2:
            value = ( float(value_list[0])+float(value_list[1]) )/2
        else:
            value = float(value_list[0])
        count += 1
        if re.search("元", i[0]):
            value /= 10000
        if re.search("千", i[0]):
            value /= 10
        if re.search("日", i[0]):
            value *= 30
        if re.search("年", i[0]):
            value /= 12
        # print(value)
        total += value

    # print(total)
    # print(count)

    print("python开发工程师平均薪资为%.2f万/月"%float(total/count))
