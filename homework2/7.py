#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 7.py
@time: 2020/3/10  18:02
"""

# 7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;
#    A---成绩>=90;
#    B-->成绩在 [80,90)
#    C-->成绩在 [70,80)
#    D-->成绩<70

import random

def grade( list1 ):
    for i in range( len(list1) ):
        if list1[i] < 70:
            list1[i] = 'D'
        elif list1[i] < 80:
            list1[i] = 'C'
        elif list1[i] < 90:
            list1[i] = 'B'
        else:
            list1[i] = 'A'


list1 = []

for i in range(20):
    list1.append( random.randint(0,100) )

print(list1)
grade(list1)
print(list1)
