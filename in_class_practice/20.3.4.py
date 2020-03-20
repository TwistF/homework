#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 20.3.4.py
@time: 2020/3/4  7:51
"""

'''
xlist = (input("请输入:").split(" "))

print(tuple(xlist))
'''

'''
a = float(input("请输入苹果重量:"))
b = float(input("请输入苹果单价:"))

print("应付款%.2f"%(a*b))
'''

'''
username = input('username:')
password = input('password:')
print(username,password)
'''

"""
name = input("name:")
age = input("age:")
skill = input("skill:")
salary = input("salary:")
info = ''' --- info of ''' + name + ''' name: ''' + name + ''' age: ''' + age + ''' skill: ''' + skill + ''' salary: ''' + salary + ''' '''
print(info)
"""

"""
name = input("name:") 
age = input("age:")
skill = input("skill:")
salary = input("salary:")
info1 = ''' --- info of %s --- Name:%s Age:%s Skill:%s Salary:%s ''' % (name,name,age,skill,salary)
print(info1)
"""

"""
name = input("username：")
age = input("age：")
skill = input("skill：") 
salary = input("salary：")
info = ''' --- info of {_name} Name：{_name} Age：{_age} Skill：{_skill} Salary：{_salary} '''.format(_name=name, _age=age, _skill=skill, _salary=salary)
print(info)
"""

"""
name = input("name：") 
age = input("age：") 
skill = input("skill：") 
salary = input("salary：") 
info = ''' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '''.format(name, name, age, skill, salary) 
print(info)
"""

"""
alist = list(range(10))

for x in alist:
    if( x % 2 == 0):
        print(x,end = " ")
"""

"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
"""