#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 5.py
@time: 2020/3/10  17:50
"""

# 5  写函数，检查传入字典的每一个value长度，
# 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;

def cut( dict ):
    for i in dict.keys():
        if len( dict[i] ) > 2:
            dict[i] = dict[i][0:2]
    return dict

# dict1 = {"1121": "1111", "22": "1"}
# dict1 = cut(dict1)
# print(dict1)

# PS:因为题目写的是“长度”，所以把value当作str简化处理
# 如果num也符合要求的话可能需要再添加几个情况