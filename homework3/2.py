#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 2.py
@time: 2020/3/23  1:18
"""

f1 = open(r'.\input.txt', 'r', encoding='utf-8')

list1 = f1.readlines()

i = 1
for str in list1:
    print('%d.%s'%(i,str), end='')
    i += 1
