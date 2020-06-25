#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: db_connect.py
@time: 2020/6/14  18:07
"""
import pymysql
from src import config

def connect():
    try:
        connect = pymysql.connect(host = config.host, user = config.user,
                                  password = config.password, database = config.database)
        cursor = connect.cursor()
        print("链接成功")
        return (connect ,cursor)
    except Exception as e:
        print("链接失败:",e)
        exit()

def read_urls(cursor, connect):
    sql = "SELECT url FROM urls"
    try:
        cursor.execute(sql)
        connect.commit()
        res = cursor.fetchall()
        return res
    except Exception as e:
        print("出现异常:",e)
        connect.rollback()

def read_salaries(cursor, connect):
    sql = "SELECT salary FROM salaries"
    try:
        cursor.execute(sql)
        connect.commit()
        res = cursor.fetchall()
        return res
    except Exception as e:
        print("出现异常:",e)
        connect.rollback()

def write_salaries(salary, cursor, connect):
    sql = """INSERT INTO salaries (id,salary) VALUES (0,%s)"""
    try:
        cursor.execute(sql, salary)
        connect.commit()
        return True
    except Exception as e:
        print(salary)
        print("操作出现错误:",e)
        return False

# connections = connect()
# connect = connections[0]
# cursor = connections[1]
#
# read_urls()
# write_salaries("1.4万/月")