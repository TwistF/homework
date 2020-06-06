#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 3.py
@time: 2020/6/4  16:27
"""

###########################################

# 运行特定功能时会出现warning，但功能均正常运行，没有受影响
# 查询后发现好像是和mysql的链接方式有关，
# 但都是在使用pymysql时出现该问题，不知道为什么使用sqlalchemy时也会
# 只能暂时对warning视而不见了，很遗憾

###########################################

import sqlalchemy
from sqlalchemy import Column, String, Integer
import datetime
from sqlalchemy.ext.declarative import declarative_base # 不具体调用好像调用不了

DIALECT = "mysql"
DRIVER = "pymysql"
USERNAME = "root"
PASSWORD = "password"
HOST = "localhost"
PORT = "3306"
DATABASE = "test"
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=GBK".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

Base = declarative_base()

class note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    text = Column(String(255), nullable=True)
    name = Column(String(30), nullable=True)
    time = Column(String(20), nullable=True)
    deleted = Column(Integer, nullable=True)

# def action(sql, *args):   # 进行操作，同时确认是否成功执行
#     try:
#         cursor.execute(sql, args)
#         connect.commit()
#         return True
#     except Exception as e:
#         print("操作出现错误:",e)
#         return False

def add():
    text = input("请输入留言:")
    name = input("请输入姓名:")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        new = note(name=name, text=text, time=time, deleted=0)
        session.add(new)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False

def delete():
    id = input("请输入要删除留言的ID:")
    try:
        res = session.query(note).filter_by(id=id).first()
        res.deleted = 1
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False

def update():
    id = input("请输入要修改留言的ID:")
    text = input("请输入要修改的内容:")
    try:
        res = session.query(note).filter_by(id=id).first()
        res.text = text
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False

def search(): # action函数不能返回结果，所以得重新写执行sql的代码
    id = input("请输入要查询的ID:")
    try:
        res = session.query(note).filter_by(id=id).one()
        session.commit()
        if res.deleted == 1:
            print("该留言已删除")
            return False
        else:
            print("留言内容为:",res.text)
            return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    try:
        engine = sqlalchemy.create_engine(DB_URI)
        DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
        session = DBSession()
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
    except Exception as e:
        session.close()
        print("数据库连接错误:",e)
        print("即将关闭数据库")
