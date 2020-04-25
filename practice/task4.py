#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task4.py
@Time : 2020/04/24 00:15:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
      封装方法，求单个学生的总分，平均分，以及打印学生的信息。
'''

class student(object):
      def __init__(self,name,age,gender,E_score,M_score,C_score):
            self._name = name
            self._age = age
            self._gender = gender
            self._E_score = E_score
            self._M_score = M_score
            self._C_score = C_score
      def totall(self):
            num = self._E_score+self._C_score+self._M_score
            print("总分为：{}".format(num))
      def average(self):
            num = (self._E_score+self._C_score+self._M_score)/3
            print("平均分为：{}".format(num))
      def massage(self):
            print("姓名：{}".format(self._name))
            print("年龄：{}".format(self._age))
            print("性别：{}".format(self._gender))
            print("英语成绩：{}".format(self._E_score))
            print("数学升级：{}".format(self._M_score))
            print("语文成绩：{}".format(self._C_score))

a = student("李四",20,"男",90,100,110)
a.totall()
a.average()
a.massage()