#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 6.py
@time: 2020/4/10  19:44
"""

class editor:
    def __init__(self, url):
        self.url = url

    def append(self,  list): # 输入信息放在list里
        f = open(self.url, 'a', encoding='utf-8')
        f.write("%s %s %s %s\n"%tuple(list))
        f.close()

    def delete(self, keyword): # keyword可以为任意信息
        f = open(self.url, 'r', encoding='utf-8')
        list = f.read().splitlines()
        f.close()
        flag = 1
        for i in list:
            if keyword in i:
                list.remove(i)
                flag = 0
        if flag == 1:
            print("未找到关键词")
            return
        f = open(self.url, 'w', encoding='utf-8')
        for i in list:
            f.write(i+'\n')

    def edit(self, keyword, pos, new): # pos代表修改位置，0~3依次为 班级 学号 姓名 成绩
        f = open(self.url, 'r', encoding='utf-8')
        list = f.read().splitlines()
        f.close()
        flag = 1
        for i in range(len(list)):
            if keyword in list[i]:
                split = list[i].split()
                split[pos] = new
                new_str = "%s %s %s %s"%tuple(split)
                list[i] = new_str
                flag = 0
        if flag == 1:
            print("未找到关键词")
        f = open(self.url, 'w', encoding='utf-8')
        for i in list:
            f.write(i+'\n')

    def search(self, keyword):
        f = open(self.url, 'r', encoding='utf-8')
        list = f.read().splitlines()
        f.close()
        flag = 1
        for i in list:
            if keyword in i:
                print(i)
                flag = 0
        if flag == 1:
            print("未找到关键词")
        else:
            print("班级 学号 姓名 成绩")

editor1 = editor(r".\test_stu.txt")
editor1.append(["class2", "1100", "Li", "100"])
editor1.delete("class3")
editor1.edit("class1", 2, "Sunny")
editor1.search("class2")
