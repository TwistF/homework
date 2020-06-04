#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 2.py
@time: 2020/6/4  23:17
"""

# 基本照搬课件上的示例代码

import socket

def reciever():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('127.0.0.1', 4869)
    # print(local_addr)
    udp_socket.bind(local_addr)

    recv_data = udp_socket.recvfrom(4048)

    print(recv_data)

    udp_socket.close()

if __name__ == "__main__":
    reciever()