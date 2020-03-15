#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 10.py
@time: 2020/3/10  17:08
"""

# 10  给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
#  提示：可以用字典来统计：key 是单词，value 是单词出现次数；
#    先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断：
#    如果字典中 key 已经出现了这个单词，那么它对应的 value ，也就是出现次数就 +1；
#    如果这个单词没出现过，就直接 插入这个单词及 value 为 1 到 字典中

text = "i can because i believe i can"
spl = text.split()

dict1 = {}

for i in spl:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

ans = sorted(dict1.items(), key = lambda x: x[1], reverse = True)

for i in ans:
    print("单词:%s   出现次数:%d" %i)