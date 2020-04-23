#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task2.py
@Time : 2020/04/22 22:23:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
'''
##提醒自己，日志还是看不大懂，有时间多看看
import logging

def log(func):
    def wrapper():
        func()
        with open(r'E:\Python\CodeProjects\PythonProjects\opms\homework5\log.txt','a') as f:
            f.write(func.__name__+'\n')
    return wrapper

@log
def function():
    for i in range(1,6):
        print(i)
    print("函数运行了")        

function()

