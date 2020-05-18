#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 2.py
@time: 2020/4/25  15:13
"""

# 已知的诸多缺陷：代码运行过慢，检索成功率低（很少有网页包含给定的关键词）



from bs4 import BeautifulSoup
import  requests
import  re
from urllib.error import URLError,HTTPError

f1 = open(r'.\urls.txt', 'r', encoding='utf-8')
list1 = []
list1 = f1.read().splitlines()
f1.close()
f2 = open(r'.\test2_result.txt', 'a', encoding='utf-8')
for i in list1:
    url = i
    print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers).content.decode('utf-8')
    except Exception:
        continue
    # print(r)
    # print(type(r))

    ret = re.finditer("http://[0-9a-zA-Z_\.\-]*\.[com,cn,net,html]{1,3}", r) # 筛选主页面中的链接

    list_url = []
    for i in ret:
        if i.group() not in list_url:
            list_url.append(i.group()) # 存储链接

    bs = BeautifulSoup(r, 'html.parser')
    f2.write(str(bs.title)+"的企业主页是:")
    print(str(bs.title)+"的企业主页是:")

    flag = 0
    for i in list_url:
        try:
            r = requests.get(i, headers=headers).content.decode('utf-8')
        except Exception:
            continue
        bs = BeautifulSoup(r, 'html.parser')

        if '企业' in str(bs.title) or '我们' in str(bs.title) or '发展' in str(bs.title):
            f2.write(i+'\n')
            print(i+'\n')
            flag = 1
            break

    if flag == 0:
        f2.write("未找到\n")
        print("未找到\n")

f2.flush()
f2.close()