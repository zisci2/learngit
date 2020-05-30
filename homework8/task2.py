#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task2.py
@Time : 2020/05/23 18:05:00
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   请查资料，Python的 requests库，如何判断一个网址可以访问；
提示 ：使用requests模块
   def getHtmlText(url):
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)    # 查一下这个方法的使用
        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
         return "产生异常"
  数据文件（1000个网址）：

'''

import requests
from multiprocessing import Pool
import os

def getHtmlText(url):
   try:
      r = requests.get(url,Timeout=30)
      r.raise_for_status()
      r.encoding = r.apparent_encoding
      print("可以访问")
      return r.text
   except :
      print("{}网址不可访问".format(url))


def getUrl():
   list = []
   try:
      with open('url_data.txt') as f:
         for line in f.readlines():
                list.append(line)
   except :
      print("文件不存在")
   return list

def M_Thread(name,url):
       getHtmlText(url)
       


if __name__ == "__main__":
   list_Thread = ['thread_1','thread_2','thread_3','thread_4','thread_5']
   pool = Pool(100)
   URL = getUrl()
   i = 0
   for url in getUrl():
          url = url.split(";")
         #  print(url[0])
          pool.apply_async(M_Thread,(list_Thread[i],url[0]))  #这。。。不能访问的有点多啊
          i += 1
          if i >= 4:
                 i=0

   print("-----开始-----")
   pool.close()
   pool.join()
   print("---完事收工---")       

