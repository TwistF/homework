#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 8.py
@time: 2020/3/28  20:05
"""

import os
import random
file1 = open(r'.\ip.txt', 'w', encoding='utf-8')
for i in range(1200):
    num = random.randint(1,254)
    num = str(num)
    ip = '172.25.254.'+num
    file1.write(ip+'\n')

    ans_dict = {}

file1.close()
file2 = open(r'.\ip.txt', 'r', encoding='utf-8')
list1 = file2.read().splitlines()
for i in list1:
    if i in ans_dict:
        ans_dict[i] += 1
    else:
        ans_dict[i] = 1
ans_dict = sorted(ans_dict.items(), key = lambda x: x[1], reverse=True)
for i in range(10):
    print(ans_dict[i])