#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 9.py
@time: 2020/3/10  17:02
"""

# 9 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；

import random

N = int(input("请输入猜测次数N:"))

num = random.randint(1,10)

flag = 0

#print(num) 测试用

for i in range(N):
    cur = int(input("请猜测1到10中的一个数:"))
    if cur == num:
        print("恭喜答对")
        flag = 1
        break
    else:
        print("很遗憾，请再试一次")

if flag == 0:
    print("您失败了")