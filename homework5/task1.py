#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task1.py
@Time : 2020/04/22 22:22:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
1  编写一个装饰器，能计算其他函数的运行时间；
'''

import  time

def display_time(func):
    def Time(*args):
        t1 = time.time()
        num = func(*args)     #*args表示任何多个自无名参数，它是一是个tuple,**kwargs表示关键字参数，它是一个dict
        t2 = time.time()
        print("函数运行耗费{0:0.4}s".format(t2-t1))
        return num
    return Time

def zhishu(num):
    if num < 2:  #大于0才有可能是素数
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i ==0:
                return False
        return True

@display_time
def count(num):
    Count = 0
    for i in range(2,num):   
        if zhishu(i):
            Count +=1
    return Count

print("{}里的素数有{}个".format(1000,count(1000)))