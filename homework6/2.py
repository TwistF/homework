#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 2.py
@time: 2020/4/10  0:56
"""

class Student:
    def __init__(self,name,age,score_C,score_M,score_E):
        self.name = name
        self.age = age
        self.score_C = score_C
        self.score_M = score_M
        self.score_E = score_E

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        if self.score_C >= self.score_M:
            if self.score_C >= self.score_E:
                return self.score_C
            else:
                return self.score_E
        else:
            if self.score_M >= self.score_E:
                return self.score_M
            else:
                return self.score_E


stu_a = Student('Li',18,98,96,99)
print(stu_a.get_age())
print(stu_a.get_name())
print(stu_a.get_course())
