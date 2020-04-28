#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 1.py
@time: 2020/4/19  12:44
"""

import re

list_origin = []
f1 = open(r'.\webspiderUrl.txt', 'r', encoding='utf-8')
list_origin = f1.read().splitlines()
f1.close()
#print(list_origin)

list_ans = []
for i in list_origin:
    # print(i)
    ret = re.search(r"http://[0-9a-zA-Z_\.\-]*\.[com,cn,net]{1,3}", i)
    if ret:
        list_ans.append(ret.group())
#print(list_ans)

f1 = open(r'.\urls.txt', 'w', encoding='utf-8')
for i in list_ans:
    f1.write(i+'\n')

# ret = re.search(r'http://[0-9a-zA-Z_\.\-]*\.[com,cn,net]{1,3}', "INSERT INTO `temp_icp_web` VALUES ('9988', '68596', '北京百姓都市生态科技有限公司', 'http://www.ok188888.cn')")
# print(ret.group())
