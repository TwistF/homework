#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 3.py
@time: 2020/5/1  22:11
"""

import requests
import re
import wget


url = 'http://www.listeningexpress.com/studioclassroom/ad/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
}

r = requests.get(url, headers=headers).content.decode('GBK') # utf-8解码报错

# print(r)
ret = re.finditer("sc[0-9a-zA-Z\s\.\-]*\.mp3", r)

front = 'http://www.listeningexpress.com/studioclassroom/ad/'

for i in ret:
    url = front+i.group() # 尝试过写quote，但反而会报错
    # print(url)
    filePath = r'.\songs\%s'%i.group()
    wget.download(url)  # 安装pywget后直接可以import wget，很方便
                        # 设置参数应该可以指定输出位置，未指定时下载至运行位置




