#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: human.py
@time: 2020/4/10  18:49
"""


class Human:
    def __init__(self, no):
        self.no = no
        self.attack = 10
        self.health = 100
        self.alive = True

    def hurt(self, damage):
        self.attack -= 2
        if self.attack < 1:
            self.attack = 1     #为避免游戏结束不了，设定攻击力最低为1
        self.health -= damage
        if self.health <= 0:
            self.alive = False