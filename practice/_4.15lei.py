#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : lei.py
@Time : 2020/04/08 09:12:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
练习:  
 定义一个dog类(颜色, 名称), 里面有一个狗叫的方法; 
 不同的狗叫声可能不一样;  然后实例化几条狗,
  然后统计实例化狗的数量
'''
class Dog():
    count = 0
    color =" "
    name = " "

    def dog(self,color,name):
        self.color = color
        self.name = name
        self.count += 1
        print("{}在叫".format(self.name))

t = Dog()
t.dog("黑色","黑子")
print(t.count)
print(t.color)
print("*"*50)
t.dog("红色","红子")
print(t.count)
print(t.color)
