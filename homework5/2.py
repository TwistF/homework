#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 2.py
@time: 2020/4/3  22:23
"""

import logging

def logger(func):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename= r'.\test.log',
                        filemode='w')
    def inner():
        func()
        logging.info('%s被调用'%func.__name__)
    return inner

@logger
def dosomething():
    return 1
