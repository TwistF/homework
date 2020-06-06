#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 2.py
@time: 2020/6/4  16:27
"""

# cursor,conn = '' # 仅为了消除报错

import pymysql
import datetime

def connect():
    try:
        connect = pymysql.connect(host='localhost', user='root',
                                  password='password', database='test')
        cursor = connect.cursor()
        print("链接成功")
        return (connect ,cursor)
    except Exception as e:
        print("链接失败:",e)
        exit()


def action(sql, *args):   # 进行操作，同时确认是否成功执行
    try:
        cursor.execute(sql, args)
        connect.commit()
        return True
    except Exception as e:
        print("操作出现错误:",e)
        return False

def add():
    text = input("请输入留言:")
    name = input("请输入姓名:")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql =  """INSERT INTO note (text, name, time, deleted) VALUES (%s, %s, %s, %s)"""
    return action(sql, text, name, time, 0)

def delete():
    id = input("请输入要删除留言的ID:")
    sql = "UPDATE note SET deleted=1 WHERE id=%s"
    return action(sql, id)

def update():
    id = input("请输入要修改留言的ID:")
    text = input("请输入要修改的内容:")
    sql = "UPDATE note SET text=%s WHERE id=%s"
    return action(sql, text, id)

def search(): # action函数不能返回结果，所以得重新写执行sql的代码
    id = input("请输入要查询的ID:")
    sql = "SELECT text, deleted FROM note WHERE id=%s"
    try:
        cursor.execute(sql, (id,))
        connect.commit()
        res = cursor.fetchone()
        if res:
            if res[1] == 0 :
                print("查找到的留言为:",res[0])
            else:
                print("该记录已被删除")
        else:
            print("未找到ID为此的留言")
    except Exception as e:
        print("出现异常:",e)
        connect.rollback()

if __name__ == '__main__':
    connections = connect()
    connect = connections[0]
    cursor = connections[1]

    while True:
        print("请输入数字来进行操作: 1:添加评论 2:删除评论 3:修改评论 4:查找评论 0:退出")
        choice = input()
        if choice == '1':
            if add():
                print("操作成功")
        elif choice == '2':
            if delete():
                print("操作成功")
        elif choice == '3':
            if update():
                print("操作成功")
        elif choice == '4':
            search()
        elif choice == '0':
            print("已退出留言板")
            break
        else:
            print("不支持的指令,请重新输入")