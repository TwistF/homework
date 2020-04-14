#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 3.py
@time: 2020/4/10  1:08
"""

class Student:
    def __init__(self,name,age,score_C,score_M,score_E):
        self.__name = name
        self.__age = age
        self.__score_C = score_C
        self.__score_M = score_M
        self.__score_E = score_E

    def sum(self):
        return self.__score_C + self.__score_E + self.__score_M

    def avr(self):
        return (self.__score_C + self.__score_E + self.__score_M)/3.0

    def print(self):
        print("name:%s"%self.__name)
        print("age:%d"%self.__age)
        print("chinese:%d"%self.__score_C)
        print("math:%d"%self.__score_M)
        print('english:%d'%self.__score_E)

stu1 = Student('Li',18,99,98,97)
print(stu1.sum())
print(stu1.avr())
stu1.print()