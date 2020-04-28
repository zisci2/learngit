#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : zhengzhe.py
@Time : 2020/04/15 09:08:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

''''
练习:
题目1：匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com

'''

import re

def main():
    ret = input("请输入邮箱地址：")
    # 如果在正则表达式中用到一些普通符号，如“。” “？”，仅需在字母前加一个反斜杠
    a = re.match(r"^[a-zA-Z_0-9]{4,20}@163\.com$",ret)
    if a:
        print("没有问题")  
    else:
        print("有问题")

if __name__ ==  "__main__":
    print("$"*50)
    main()