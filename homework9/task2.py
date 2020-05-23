#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task2.py
@Time : 2020/05/17 14:37:26
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；
'''
from socket import *

def main():
    upd_socket = socket(AF_INET,SOCK_DGRAM)
    local_addr = ("192.168.43.89",6677)
    upd_socket.bind(local_addr)
    while True:   
        recv_data = upd_socket.recvfrom(1024)
        print(recv_data)
        print(recv_data[0].decode('gbk'))  #不可utf-8
        print(recv_data[1])
        if recv_data == None:
            upd_socket.close()
    

if __name__ == "__main__":
    main()
