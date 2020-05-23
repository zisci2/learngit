#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task4.py
@Time : 2020/05/17 14:51:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
4 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；
  参考文档：https://blog.csdn.net/CxsGhost/article/details/103319864
'''
import socket,get,threading,os

class ChatSever:
  def __init__(self):
    self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    self.addr = (get.get_ip(),10000)
    self.users = {}

  def start_sever(self):
    try:
      self.socket.bind(self.addr)
    except Exception as e:
      print("出现问题：%s"%e)

    #self.socket.listen(5)  #步行啊
    print("服务器已开始，请等待连接...")
    print("在空白处输入stop sever并回车，关闭服务器...")
    #self.accept_count()

  def accept_count(self):
    while True:
      s,addr = self.socket.accept()
      self.users[addr] = s
      number = len(self.users)
      print("用户{}连接成功！先共有{}名用户".format(addr,number))
      threading.Thread(target=self.recv_send,args=(s.addr)).start()

  def recv_send(self,socket,addr):
    while True:
      try:
        response = socket.recv(4096).decode("gbk")
        msg = "{}用户{}发来消息:{}".format(get.get_time,addr,response)
        for client in self.users.values():
              client.send(msg.encode("gbk"))
      except ConnectionAbortedError:
        print("用户{}已经退出聊天！".format(addr))
        self.users.pop(addr)
        break

  def close_sever(self):
        for client in sever.users.values():
              client.close()
        self.socket.close()
        os._exit(0)

if __name__ == "__main__":
    sever = ChatSever()
    sever.start_sever()
    while True:
          cmd = input()
          if cmd == 'stop sever':
                sever.close_sever()
          else:
                print("输入指令无效，请重新输入")
