#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 20.4.3.py
@time: 2020/4/3  8:36
"""

# def createCounter():
#     a = 0
#     def counter():
#         nonlocal a
#         a += 1
#         return a
#     return counter
#
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

import  logging

# def logger(func):
#     def inner()