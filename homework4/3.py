#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 3.py
@time: 2020/3/28  15:09
"""

import hashlib
import os
list1 = []
for i in range(5):
    name = input("请输入第%d个同学的姓名:"%(i+1))
    account = input("请输入第%d个同学的账号:"%(i+1))
    passw = input("请输入第%d个同学的密码:"%(i+1))
    md5 = hashlib.md5()
    md5.update(passw.encode('utf-8'))
    passw_md5 = md5.hexdigest()
    list1.append((name, account, passw_md5))

file1 = open(r'.\test.txt','w', encoding='utf-8')
for i in list1:
    for str in i:
        file1.write(str+' ')
    file1.write('\n')

file1.close()
