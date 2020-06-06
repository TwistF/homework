#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 4.py
@time: 2020/6/5  14:02
"""

# 搬自homework9

import socket
import threading
import time

def server(): # 基本和test2一样
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('127.0.0.1', 4869)
    # print(local_addr)
    udp_socket.bind(local_addr)
    while True:
        recv_data = udp_socket.recvfrom(4048)
        print("收到消息来自{}: {}".format(recv_data[1], recv_data[0]))
    udp_socket.close()

def client(): # 基本和test1一样
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_addr = ('127.0.0.1', 4869)
    while True:
        send_data = input("请输入要发送的数据:")
        udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
        time.sleep(1)
    udp_socket.close()

if __name__ == "__main__":
    t = threading.Thread(target= server)
    t.start()
    client()