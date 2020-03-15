#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 1.py
@time: 2020/3/10  15:34
"""

# 1 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；

list1 = []
list2 = []
list3 = []
list4 = []

for x in range(51):
    if x % 2 == 1:
        list1.append(x)
    if x % 2 == 0:
        list2.append(x)
    if x == 0 or x == 1:  #避免除法运算的问题
        continue
    flag = 0
    for i in range(2,x):
        if x % i == 0:
            flag = 1
    if flag == 0 :
        list3.append(x)
    if x%2 == 0 and x%3 == 0:
        list4.append(x)

print("奇数:",list1)
print("偶数:",list2)
print("质数:",list3)
print("同时被2和3整除的数:",list4)