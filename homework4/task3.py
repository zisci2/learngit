#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task3.py
@Time : 2020/04/18 13:07:14
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
        Tom   admin   XXXXX
        Jack   root      XXXXX   
'''

import hashlib

# with open(r"","w",encoding='utf-8') as f:
#         f

num = int(input("请问需要存入几个人的账户、密码？"))
i = 1
list = []
while i<=num:
        i +=1
        name = input("请输入姓名：")
        account = input("请输入账户：")
        mima = input("请输入密码：")
        password = hashlib.sha1()
        password.update(mima.encode('utf-8'))
        a = (name,account,password.hexdigest())
        print(a)
        list.append(a)

with open(r"E:\Python\CodeProjects\PythonProjects\opms\homework4\学生信息.txt","w+",encoding='utf-8') as f:
        for i in list:
                # print(i[0],i[1],i[2])
                f.write(i[0]+' ')
                f.write(i[1]+' ')
                f.write(i[2]+'\n')

print("数据存入成功！")
        
        
        