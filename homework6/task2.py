#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task2.py
@Time : 2020/04/24 00:14:53
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
二 定义一个学生Student类。有下面的类属性：
1 姓名 name
2 年龄 age
3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
'''

# class studen():
#     name = ''
#     age = 0
#     score = []
#     def get_name(self,n):
#         return self.name = n
#     def get_age(self,a):
#         return self.age = a
#     def get_course(self,s):
#         return self.score = s

# stu1 = studen('张三',19,(23,45,76))


##提醒自己：以上是错误示范，再来

class studen(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return self.score
    
stu1 = studen("法外狂徒张三",24,(67,78,89))  #因为stu1 = studen(("法外狂徒张三",24,(67,78,89)))多了个括号，然后就会出现缺少参数的情况，记住
print("学生信息如下")
print("学生姓名:{}".format(stu1.get_name()))
print("学生年龄:{}".format(stu1.get_age()))
print("学生语数英成绩:{}".format(stu1.get_course()))
