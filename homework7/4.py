#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 4.py
@time: 2020/5/2  1:29
"""

import requests
from bs4 import BeautifulSoup

urls = []
url = "https://www.programcreek.com/python/index/7386/tensorflow" # 只选取了部分子页面
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
}

try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.content, "lxml")
    # print(soup)
    content = soup.find("div", id="content").ul.find_all("li")
    for i in content:
        urls.append(i.find('div').a.attrs['href'])
except Exception as e:
    print("链接至网页失败.", e)


for url in urls:
    print(url)
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.content, "lxml")

    r_main = soup.find('div', id='content').find('div', id='main')
    # print(r_main)

    examples = soup.find_all('div', attrs={'class': 'examplebox'})
    try:
        with open(r'.\examples.txt', 'w', encoding='utf-8') as f1:
            f1.write('********************************\n')
            f1.write(r_main.h1.span.string)
            # print(r_main.h1.span.string)
            for i in examples:
                title = i.find("div", attrs={'class': 'exampleboxheader'})
                f1.write(title.table.tbody.tr.td.span.string+'\n')
                # print(f1.write(title.table.tbody.tr.td.span.string+'\n'))

                content = i.find("div", attrs={'class': 'exampleboxbody'})
                pre = content.pre
                for i in pre.children:
                    f1.write(i.string+'\n\n\n')
                f1.flush()
    except Exception as e:
        print(e)
        continue




