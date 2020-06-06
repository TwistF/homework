#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 2.py
@time: 2020/6/5  14:02
"""

import requests
from threading import Thread

def multi_check(url_list, fir, last):
    def check(url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            return True
        except:
            return False
    for i in range(last-fir):
        if check(url_list[fir+i]):
            print("%s访问成功"%url_list[fir+i])
        else:
            print("%s访问超时"%url_list[fir+i])


if __name__ == '__main__':
    with open(r'.\url_data.txt', 'r') as f:
        url_list = f.read().splitlines()
        # print(url_list)
    dist = int(len(url_list) / 10)
    for i in range(10):
        t = Thread(target=multi_check, args=(url_list, i*dist, (i+1)*dist -1))
        t.start()
