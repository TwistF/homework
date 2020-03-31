#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 4.py
@time: 2020/3/23  1:56
"""

import os

origin_files = os.listdir(r'.\img')
for i in origin_files:
    name = os.path.splitext(i)
    if name[1] == '.jpg' or name[1] == '.JPG':
        continue
    os.rename(i, name[0] + '.jpg')