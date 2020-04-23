#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task3.py
@Time : 2020/04/22 22:23:53
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
'''

def judge(func):
    def wrapper(*args,**kwargs):
        list = []
        with open(r"E:\Python\CodeProjects\PythonProjects\opms\homework5\user.txt",'r',encoding='utf-8') as f:
            for line in f.readlines():   ##为什么用readline()不行呢？？？？呈现一个字母为一个元素  ps数据是自己存进去，不是代码存入
                line.strip('\n')
                line1 = line.split()
                print("悄悄提醒一下，账户密码为{}".format(line1))
                list.append(line1)
        account = input("请输入账户:")
        for i in list:
            if account == i[0]:
                password = input("请输入密码：")
                if password == i[1]:
                    func()
                    break   ##为什么需要加一个break呢？不加的话会打印“输入账户有误”这句话，if else语句没有了吗
                else:
                    print("输入的密码有误！")
                    break
            else:
                print("输入账户有误！")
                break
    return wrapper

@judge
def Function():
    for i in range(6):
        print("可以使用函数啦开不开心")


Function()