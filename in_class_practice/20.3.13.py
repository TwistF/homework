#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 20.3.13.py
@time: 2020/3/13  8:29
"""

"""
lst = [('a', 90), ('b', 80.3), ('c', 69.4), ('d', 76.2)]

lst.sort(key=lambda k: k[1])

for x in range(len(lst)):
    print("%s %.2f"%lst[x])
"""

a = 1
b = 2
a,b = b,a

print("a的值为:",a)
print("b的值为:",b)