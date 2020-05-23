#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : udp_receive.py
@Time : 2020/05/19 14:05:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# UDP 接收网络数据

from socket import *

def main():
   # 绑定端口信息
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    
    local_addr=('',9999)

    udp_socket.bind(local_addr)
   # 接收数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
   # 打印显示接收到的数据
    print(recv_data)

    #print(recv_data[0].decode('gbk'))
    #print(recv_data[1])

   # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()