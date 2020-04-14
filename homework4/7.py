#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 7.py
@time: 2020/3/28  19:51
"""

import os

def pack(path):
    list1 = os.listdir(path)
    total = 0
    for i in list1:
        if(os.path.isfile(i)):
            total += os.path.getsize(i)
        else:
            #print(r"%s"%os.path.join(path, i))
            total += pack(r"%s"%os.path.join(path, i))
    return total

#print(pack(r"C:\Users\47539\PycharmProjects\untitled1\homework4"))