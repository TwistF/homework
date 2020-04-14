#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 1.py
@time: 2020/4/3  20:26
"""

import time

def timer(func):
    def inner():
        time1 = time.time()
        func()
        time2 = time.time()
        print("运行时长为%s"%(time2-time1))
    return inner

@timer
def dosomthing():
    return 1

