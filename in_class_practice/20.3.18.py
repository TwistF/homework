#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 20.3.18.py
@time: 2020/3/18  8:29
"""

import os

# pwd = os.path.abspath('.')
# print(pwd)

# print(os.path.basename(r'C:\Users\47539\PycharmProjects\untitled1\test.txt'))  # 返回文件名
# print(os.path.dirname(r'C:\Users\47539\PycharmProjects\untitled1\test.txt'))  # 返回目录路径
# print(os.path.split(r'C:\Users\47539\PycharmProjects\untitled1\test.txt'))  # 分割文件名与路径
# print(os.path.join(r'C:\Users\47539\PycharmProjects\untitled1', 'first', 'test.txt'))  # 将目录和文件名合成一个路径



# f = open(r'C:\Users\47539\PycharmProjects\untitled1\test.txt', 'r')
# print(f.read())
#
# with open(r".\test.txt","r") as file:
#     print(file.read())
#
# with open(r"..\1\test.txt","r") as file:
#     print(file.read())



f = open(r'.\test.txt', 'r', encoding='utf8')
list1 = f.readlines()
f.close()

list2 = []
for i in list1:
    list2.append(tuple(i.split()))

ans = sorted(list2, key = lambda x: x[2], reverse = True)
f = open(r'.\test1.txt', 'w', encoding='utf8')
for i in ans:
    f.write("%s     %s     %s\n" %i )




