#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 7.py
@time: 2020/3/23  2:44
"""

import  jieba

f1 = open(r'.\荷塘月色.txt', 'r', encoding='utf-8')

txt1 = f1.read()
for i in ',.()-"，。‘“”’（）-':
    txt1 = txt1.replace(i,' ')
#print(txt1)

char_list = jieba.lcut(txt1)
#print(char_list)

ans_dict = {}
for i in char_list:
    if i in ans_dict:
        ans_dict[i] += 1
    else:
        ans_dict[i] = 1

ans_dict = sorted(ans_dict.items(), key = lambda x: x[1], reverse=True)
#print(ans_dict)

print("词语,次数")
for i in range(20):
    cur = ans_dict[i]
    print('%s,%d'%cur)
