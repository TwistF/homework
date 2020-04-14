#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 9.py
@time: 2020/3/28  20:14
"""

import requests
import os

def download(url, path):
    if not os.path.exists(path):
        os.mkdir()
    path = os.path.join(path, "new_picture.jpg")
    pic = requests.get(url)
    file1 = open(path, 'wb')
    file1.write(pic.content)


# url = "http://n.sinaimg.cn/sinacn/w600h506/20180220/ada5-fyrswmu3894971.jpg"
# path = r"C:\Users\47539\PycharmProjects\untitled1\homework4"
# download(url, path)
