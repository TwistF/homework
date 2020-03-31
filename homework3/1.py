#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 1.py
@time: 2020/3/23  0:31
"""

list1 = []
f1 = open(r'.\input.txt', 'w', encoding='utf-8')

while True:
    cur_str = input()
    if cur_str == '':
        break
    list1.append(cur_str + '\n')

for str in list1:
    f1.write(str)

f1.close()
