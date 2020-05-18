#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 1.py
@time: 2020/5/7  1:43
"""

import random
import threading
from multiprocessing import Pool

def score( num , n):
    for i in range(num):
        print("%d号打印:"%n,random.randint(0,100))


if __name__ == '__main__':
    # 多线程
    for i in range(5):
        t = threading.Thread(target=score(20, i))
        t.start()

    print("**************************************")
    # 线程池

    po = Pool(5)
    for i in range(10):
        po.apply_async(score, (10, i))

    print("----start-----")
    po.close()
    po.join()
    print("----close-----")