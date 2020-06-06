#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 1.py
@time: 2020/6/6  13:21
"""

# 测试课件中的例子

import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_addr = ('192.168.234.1', 8080)

    send_data = input("请输入要发送的数据:")
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

    udp_socket.close()

if __name__ == "__main__":
    main()