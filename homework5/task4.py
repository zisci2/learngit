#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task4.py
@Time : 2020/04/22 22:24:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
4  编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
     三个目标函数分别为：
     A 打印输出20000之内的素数；
     B 计算整数2-10000之间的素数的个数；
     C 计算整数2-M之间的素数的个数；
  可以观看给的视频材料，仿照示例来做；
'''

#装饰器
def situation_1(func):
    def Number(*args):
        func()     
    return Number

def situation_2(func):
    def Number(*args):
        func(*args)     
    return Number

def situation_3(func):
    def Number(*args):
        num = func(*args)     
        return num
    return Number

# 判断是否为素数
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


def function_1():
    Count = 0
    for i in range(2,20000):   
        if zhishu(i):
            Count +=1
    print("2~{}共有{}个素数".format(20000,Count))

@situation_2
def function_2(num):
    Count = 0
    for i in range(2,10000):   
        if zhishu(i):
            Count +=1
    print("2~{}共有{}个素数".format(10000,Count))

@situation_3
def function_3(num):
    Count = 0
    for i in range(2,num):   
        if zhishu(i):
            Count +=1
    return Count


print("*"*28+"目标函数无参数无返回值"+"*"*28)
function_1()
print("*"*30+"目标函数有返回值"+"*"*30)
num1 = 10
function_2(num1)
print("*"*30+"目标函数有返回值"+"*"*30)
num = 5000
print("2~{}共有{}个素数".format(num,function_3(num)))
