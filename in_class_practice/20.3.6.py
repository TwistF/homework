#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 20.3.6.py
@time: 2020/3/6  7:57
"""

"""
def price_apple(weight, price):
    return weight * price

weight = int(input("苹果的重量:"))
price = int(input("苹果的单价:"))
total = price_apple(weight, price)

print("总价格为:", total)
"""

"""
def print_plus(alist):
    print(alist)
    alist.append(1)
    print(alist)

alist = [1, 2, 3]
print("append前的地址:",id(alist))

print_plus(alist)

print("append后的地址:",id(alist))
"""

"""
a = list(range(1,21))

res = list(filter(lambda x:x%2 == 1, a))

print(res)
"""


def print_x ( arg1, *args ):
    a = list(arg1)
    for x in args:
        a.append(x)
    print(a)

#print_x('a', 'b', 'c', 1)


def print_dict( arg1, **args ):
    a = arg1 + args
    print(a)


