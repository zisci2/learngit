#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task1.py
@Time : 2020/04/25 17:54:35
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
   提示，文件有1000行，注意控制每次读取的行数；
     
'''
import re
import os


def main():
   print("开始提取...")  
   print()    
   i = 0
   list = []
   string = '(http://|https://).{1,100}(\.cn|\.com|\.net|\.org|\.cc|\.vip|\.|\.top|\.shop)'   
   with open(r"webspiderUrl.txt",'r',encoding='utf-8') as f:
      for line in f.readlines():
            # print(line)
            i += 1
            aa = re.search(string,line,re.M|re.I)
            if aa:
                     list.append(aa.group())
                  # print(i,aa.group())
            else:
                     print(i,line+"没有连接")

   with open("message.txt", 'w+', encoding='utf-8') as f:
      for line in list:
             f.write(line+'\n')
   print()
   print("存入完毕！")

if __name__ == '__main__':
   main()
