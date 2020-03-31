#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 5.py
@time: 2020/3/23  2:17
"""

f1 = open(r'.\Blowing in the wind.txt', 'r', encoding='utf-8')

origin_list = f1.read().splitlines()
f1.close()
#print(origin_list)

origin_list.insert(0, "Blowin' in the wind")
origin_list.insert(1, '')  # 插入的空格都是为了保证格式
origin_list.insert(2, 'Bob Dylan')
origin_list.insert(3, '')
origin_list.append(' ')
origin_list.append('1962 by Warner Bros.Inc')

f1 = open(r'.\Blowing in the wind.txt', 'w', encoding='utf-8')
for i in origin_list:
    f1.write(i+'\n')

f1.close()

f1 = open(r'.\Blowing in the wind.txt', 'r', encoding='utf-8')
new_list = f1.read().splitlines()

for i in new_list:
    print(i)