#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 20.2.21.py
@time: 2020/2/21  8:48
"""
dict1 = {'Name': 'A', 'Age': 7, 'Class': 'First'}
#dic

dict1['Age'] = 8
dict1['School'] = 'NCEPU'

print("dict1['Age']: ", dict1['Age'])
print("dict1['School']: ", dict1['School'])

del dict1['Name']

#print("dict1['Name']:", dict1['Name'])

basket = {'AB', 'CD', 'EF'}
print(basket)
basket.pop()
print(basket)