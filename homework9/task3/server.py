#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : tsak3.py
@Time : 2020/05/17 14:38:10
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
''' 
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',1234))
print("创建UDP连接在4567端口...")
while True:
    data,addr = s.recvfrom(1024)
    print("收到来自%s的来信:%s"%(addr,data.decode('gbk')))
    reply = input("发送消息：")
    if repr == None:
        s.close()
        continue
    s.sendto(reply.encode('utf-8'),addr)  #注意encode与decode
