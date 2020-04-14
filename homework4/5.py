#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 5.py
@time: 2020/3/28  16:54
"""

import os

def copy1( path1, path2 ):
    f1 = open( path1, 'r', encoding='utf8' )
    list1 = f1.readlines()
    name = os.path.basename(path1)
    path2 = os.path.join( path2, name )
    f2 = open( path2, 'w', encoding='utf8' )
    for i in list1:
        f2.write(i)
    f1.close()
    os.remove( path1 )
    f2.close()