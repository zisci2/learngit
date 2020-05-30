#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task4.py
@Time : 2020/05/23 18:05:49
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
4 多进程通讯：
  编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息
'''
from multiprocessing import Process,Queue
import time

def receive(q):
      if not q.empty():
            value = q.get(True)
            print("接受到的信息：{}".format(value))

def send(q,n):
    q.put(n)


if __name__ == "__main__":
    q = Queue()
    while True:
      n = input("输入发送信息：")    #将你放入send函数会出现EOFError: EOF when reading a line
      s = Process(target=send,args=(q,n))
      s.start()
      s.join()

      r = Process(target=receive,args=(q,))
      r.start()
      r.join()

      