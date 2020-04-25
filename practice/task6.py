#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task6.py
@Time : 2020/04/24 00:16:41
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
六  用面向对象,实现一个学生Python成绩管理系统;
      学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
      实现对学生信息及成绩的增,删,改,查方法;
       
'''

import sys
class student(object):
      def Add(self,room,id,name,score):
            self.room = room
            self.id = id
            self.name = name
            self.score = score
            with open('students massage.txt','a+',encoding='utf-8')as f:
                  f.write(self.room+' ')
                  f.write(self.id+' ')
                  f.write(self.name+' ')
                  f.write(self.score+'\n')
            print("存入成功")

      def delete(self):
            name = input("输入你想要删除的学生的名字：")
            list = []
            num = 0
            with open('students massage.txt','r',encoding='utf-8') as f:
                  for line in f.readlines():
                        line.strip('\n')
                        a = line.split()
                        if name in a:
                              num += 1
                        if name not in a:
                              list.append(a)
            if num == 0:
                  print("查无此人")
                  print("删除失败")
            else:
                  # with open('students massage.txt','w+',encoding='utf-8')as f:
                  #       for i in list:
                  #             f.write(i)
                  # print('删除成功！')
                  ##list无法直接写入，谨记
                  with open('students massage.txt','w+',encoding='utf-8')as f:
                        for i in list:
                              f.write(i[0]+' ')
                              f.write(i[1]+' ')
                              f.write(i[2]+' ')
                              f.write(i[3]+'\n')
                  print('删除成功！')                  

      def change(self):
            name = input("请输入你想修改信息的学生的名字：")
            judge = int(input("请问你想修改的是（班级输入0，学号 1，姓名 2，python成绩 3）："))
            after = input("请输入修正的信息：")
            list = []
            num = 0
            with open("students massage.txt",'r',encoding='utf-8') as f:
                  for line in f.readlines():
                        line.strip('\n')
                        a = line.split()
                        if name in a:
                              a[judge] = after
                              num += 1
                        list.append(a)
            if num == 0:
                  print("查无此人")
                  print("修改失败")
            else:
                  with open('students massage.txt','w+',encoding='utf-8')as f:
                        for i in list:
                              f.write(i[0]+' ')
                              f.write(i[1]+' ')
                              f.write(i[2]+' ')
                              f.write(i[3]+'\n')
                  print("修改成功！")

      def search(self):
            m = input("请输入想要查询的学生姓名或学号：")
            num = 0
            with open('students massage.txt','r',encoding='utf-8') as f:
                  for line in f.readlines():
                        line.strip('\n')
                        a = line.split()
                        if m in a:
                              print("班级：{}".format(a[0]))
                              print("学号：{}".format(a[1]))
                              print("姓名：{}".format(a[2]))
                              print("python成绩：{}".format(a[3]))
                              num +=1
                              
            if num == 0:
                  print(num)
                  print("查无此人")     
            

def func():
      print("*"*15+'欢迎使用学生Python成绩管理系统'+'*'*20)
      print("*"*20+'添加学生成绩请输入1'+'*'*20)
      print("*"*20+'删除学生信息请输入2'+'*'*20)
      print("*"*20+'修改学生信息请输入3'+'*'*20)
      print("*"*20+'查询学生信息请输入4'+'*'*20)
      print("*"*22+'退出系统请输入0'+'*'*22)
      num = input("请输入：")
      AA = student()
      while not ('0' <= num <= '4'):
            num = input("输入有误，请重新输入：")
      
      if num == '0':
            print("感谢使用！")
            sys.exit()
      
      elif num == '1':
            room = input("请输入班级：")
            id = input("请输入学号：")
            name = input("请输入姓名：")
            score = input("请输入python成绩：")
            AA.Add(room,id,name,score)
            func()
      elif num == '2':
            AA.delete()
            func()
      elif num == '3':
            AA.change()
            func()
      elif num == '4':
            AA.search()
            func()


func()