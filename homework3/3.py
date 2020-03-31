#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 3.py
@time: 2020/3/23  1:27
"""

f1 = open(r'.\test3.txt', 'r', encoding='utf-8')

origin_list = f1.read().splitlines()
data_list = []

for i in origin_list:
    list2 = i.split(',')
    list2[2] = int(list2[2]) #对分数类型转化
    data_list.append(tuple(list2))

ans = sorted(data_list, key = lambda x: x[2], reverse = True)
print('学号,姓名,班级')
for i in ans:
    print('%s,%s,%d'%i)