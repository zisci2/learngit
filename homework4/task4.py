#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task4.py
@Time : 2020/04/18 13:07:26
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
4  (继续上面的练习) 模拟用户登录:
     5个同学的姓名,账号和密码(加密后的),保存在一个文件上; 
    系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  
    如果都正确,打印提示, 您登录成功(失败);
'''

'''
name = 1,
acount = 1
passwork = 1
'''


import os
import hashlib

list = []
def Read ():
    with open(r"E:\Python\CodeProjects\PythonProjects\opms\homework4\学生信息.txt","r",encoding='utf-8') as f:
        while True:
            a = f.readline()
            if not a:
                return list
            a.strip('\n')
            list1 = a.split()
            list.append(list1)

Read()
# print(list)
name = input("请输入姓名：")
for i in list:
    if name == i[0]:
        print(i[0],i[1],i[2])
        account = input("请输入账号：")
        if account == i[1]:
            mima = input("请输入密码：")
            paswork = hashlib.sha1()
            paswork.update(mima.encode('utf-8'))
            if paswork.hexdigest() == i[2]:
                print("登陆成功！")
            else:
                print("登录失败，输入密码错误！")
                break
        else:
            print("登录失败，输入账号错误！")
            break
    else:
        print("登录失败，输入姓名错误！")
##为什么if执行后else还会执行？？？？  循环对比