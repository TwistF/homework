#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 4.py
@time: 2020/4/4  0:14
"""

def functions(func):
    def inner(*args, **kwargs):
        a = func(*args, **kwargs)
        #print(a)
        print("decorated")
        if a == None:
            return
        return a
    return inner

@functions
def A():
    for i in range(2, 20001):
        flag = 0
        for j in range(1, i):
            if j != 1 and i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i)

@functions
def B():
    num = 0
    for i in range(2,10001):

        flag = 0
        for j in range(1, i):
            if j != 1 and i % j == 0:
                flag = 1
                break
        if flag == 0:
            num += 1
    return num

@functions
def C( M ):
    num = 0
    for i in range(2, M+1):
        flag = 0
        for j in range(1, i):
            if j != 1 and i % j == 0:
                flag = 1
                break
        if flag == 0:
            num += 1
    return num

A()
print(B())
print(C(10000))