#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 4.py
@time: 2020/3/28  16:27
"""

import os
import sys
import hashlib

file1 = open(r'.\test.txt', 'r', encoding='utf-8')

list_origin = file1.read().splitlines()
#print(list_origin)

list_remake = []
for i in list_origin:
    list_cur = i.split()
    list_cur = tuple(list_cur)
    list_remake.append(list_cur)

#print(list_remake)

flag = -1
while 1:
    name = input("请输入姓名:")
    for i in list_remake:
        if i[0] == name:
            flag = i
    if flag == -1:
        print("未找到该同学,请重新输入")
    else:
        break

while 1:
    account = input("请输入账号:")
    if i[1] != account:
        print("账号错误,请重新输入")
    else:
        break

while 1:
    passw = input("请输入密码:")
    md5 = hashlib.md5()
    md5.update(passw.encode('utf-8'))
    passw_md5 = md5.hexdigest()
    if i[2] == passw_md5:
        print("登录成功")
        break
    else:
        print("密码错误,请重新输入")

#测试用例 MONEY ITEM password