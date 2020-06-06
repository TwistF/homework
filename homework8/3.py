#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 3.py
@time: 2020/6/5  14:03
"""

import threading
import time
from queue import Queue

def check(x):
    if x in (1,2,3,):
        return True
    if x == 0:
        return False
    # print(x)
    for i in range(2, int(x/2)):
        if x%i == 0 :
            return False
    return True

# def timecount(f):   写了个装饰器，发现不太行
#     def f1(*agrs):
#         t1 = time.time()
#         # print("素数有%d个"%f())
#         f(*agrs)
#         t2 = time.time()
#         return t2-t1
#     return f1


def non_thread(fir, last):
    ans = 0
    for i in range(fir, last):
        if check(i):
            ans += 1
    return ans

def in_thread(fir, last, q):
    ans = 0
    for i in range(fir, last):
        if check(i):
            ans += 1
    q.put(ans)

def multi(n):
    q = Queue()
    threads = []
    ans = 0
    dist = int(100000 / n)
    for i in range(n):
        t = threading.Thread(target=in_thread, args=(i*dist, (i+1)*dist-1, q))
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    for i in  range(n):
        ans += q.get()
    print("素数个数为%d"%ans)

if __name__ == '__main__':
    t1 = time.time()
    print("素数个数为:%d"%non_thread(1, 100000))
    t2 = time.time()
    print("单线程运行时间为 %d s" %(t2-t1) )
    t1 = time.time()
    multi(4)
    t2 = time.time()
    print("4线程运行时间为 %d s" %(t2-t1) )
    t1 = time.time()
    multi(10)
    t2 = time.time()
    print("10线程运行时间为 %d s" %(t2-t1) )