#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task7.py
@Time : 2020/04/18 13:08:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
7 使用python代码统计一个文件夹中所有文件的总大小
'''

import os
def calculate(str):
    size = 0
    if os.path.isdir(str):
        path_list = os.listdir(str)
        print(path_list)
        for i in path_list:
            i = os.path.join(str,i)
            size +=os.path.getsize(i)
        return size/1024
    if os.path.isfile(str):
        return os.path.getsize(str)/1024
    else:
        print("找不到文件！")

path = "E:\Python\CodeProjects\PythonProjects\opms\homework4"
print(calculate(path),"kb")
