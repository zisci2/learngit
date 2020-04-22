#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task5.py
@Time : 2020/04/18 13:07:35
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
5  通过Python来模拟实现一个txt文件的拷贝过程;
'''

def  copy(path1,path2):
    list = []
    f1 = open(path1,"r",encoding="utf8")
    a1 = f1.read()
    f2 = open(path2,"w",encoding="utf8")
    f2.write(a1)
    print("复制成功！")


path1 = r"E:\桌面\文件夹1\test1.txt"
path2 = r"E:\桌面\文件夹2\test2.txt"
copy(path1,path2)