#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 3.py
@time: 2020/4/4  0:01
"""

def loginner(func):
    account = "administrator"
    passw = "password"
    def inner():
        a = input("请输入账号:")
        b = input("请输入密码:")
        if a==account and b==passw:
            print("登录成功")
            func()
        else:
            print("登陆失败")
            return
    return inner

@loginner
def dosomthing():
    return 1