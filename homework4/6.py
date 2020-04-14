#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 6.py
@time: 2020/3/28  19:16
"""

import os
import datetime

def pack(path):
    list1 = os.listdir(path)
    print("名称         日期                    类型    大小")
    for i in list1:
        print(i, end='')
        print('   ', end='')
        print(datetime.datetime.fromtimestamp(os.path.getatime(i)), end='')
        print('   ', end='')
        if(os.path.isfile(i)):
            print("文件    ", end='')
        else:
            print("文件夹   ", end='')
        print(os.path.getsize(i), end='')
        print('')


#pack(r"C:\Users\47539\PycharmProjects\untitled1\homework4")