#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : client.py
@Time : 2020/05/23 08:40:13
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data = input("请输入内容：").encode('utf-8')
    if data == None:
        s.close()
    else:
        s.sendto(data,('127.0.0.1',4567))
    print("接收内容：%s"%s.recv(1024).decode('gbk'))