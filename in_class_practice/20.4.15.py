#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 20.4.15.py
@time: 2020/4/15  9:10
"""

import re

def main():
    email = input("请输入邮箱地址:")
    ret = re.match(r'^[0-9a-zA-Z_]{4,20}@163\.com$',email)
    if ret:
        print("true")
    else:
        print("false")

main()