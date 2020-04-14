#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 3.py
@time: 2020/4/10  1:39
"""

class dictclass:
    def __init__(self, dict):
        self.dict = dict
    def del_dict(self, key):
        self.dict.pop(key, None)
        return self.dict
    def get_dict(self,key):
        if key in self.dict:
            return self.dict[key]
        else:
            return 'not found'
    def update_dict(self, dict):
        self.dict = {**self.dict, **dict}
        #print(self.dict)
        list1 = []
        for i in self.dict:
            list1.append(self.dict[i])
        return list1

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}

dict_p = dictclass(dict1)
print(dict_p.get_dict('b'))
print(dict_p.get_dict('c'))
print(dict_p.del_dict('a'))
print(dict_p.update_dict(dict2))