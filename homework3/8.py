#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 8.py
@time: 2020/3/23  2:51
"""

def char_count( path ):
    f1 = open(path, 'r', encoding='utf-8')

    txt1 = f1.read()
    txt1 = txt1.lower()
    for i in ',.()-"':
        txt1 = txt1.replace(i,' ')
    #print(txt1)

    char_list = txt1.split()
    #print(char_list)

    ans_dict = {}
    for i in char_list:
        if i in ans_dict:
            ans_dict[i] += 1
        else:
            ans_dict[i] = 1

    ans_dict = sorted(ans_dict.items(), key = lambda x: x[1], reverse=True)
    #print(ans_dict)

    # print("单词,次数")
    # for i in range(20):
    #     cur = ans_dict[i]
    #     print('%s,%d'%cur)
    return ans_dict

ans1 = char_count(".\paper1.txt")
ans2 = char_count(".\paper2.txt")

f1 = open(r'.\ans1.txt', 'w', encoding='utf-8')
for i in ans1:
    f1.write("%s %d"%i+'\n')
f1.close()

f2 = open(r'.\ans2.txt', 'w', encoding='utf-8')
for i in ans2:
    f2.write("%s %d"%i+'\n')
f2.close()

char_list1 = []
char_list2 = []
for i in range(10):
    char_list1.append(ans1[i][0])
    char_list2.append(ans2[i][0])
#print(char_list1)
#print(char_list2)

flag = 0
for i in char_list1:
    if i in char_list2:
        flag+=1

print("相似度为%d0%%"%flag)