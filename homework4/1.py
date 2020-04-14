#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 1.py
@time: 2020/3/27  22:35
"""

import datetime

list1 = [1]*100000000 #为了看出差别，调高了数量级

time1 = datetime.datetime.now()
list1.insert(0, 99)
list1.append(99)
time2 = datetime.datetime.now()
# print(time1)
# print(time2)
delta_time1 = time2-time1


from collections import deque

list1 = [1]*100000000

q = deque(list1)
time1 = datetime.datetime.now()
q.appendleft(99)
q.append(99)
time2 = datetime.datetime.now()
delta_time2 = time2-time1
# print(delta_time1)
# print(delta_time2)

print("deque快", end='')
print(delta_time1-delta_time2)
