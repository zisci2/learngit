# -*- encoding: utf-8 -*-
'''
@File : task8.py
@Time : 2020/03/09 01:25:38
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
8 设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；
  将这10个员工，按照工资从高到低打印输出；
   提示：可以组合使用我们的序列数据类型；
'''

# 问题不知道怎么使用序列数据，因为像列表，元组这些只能存一下数据但不知道这些数据是什么意思，所以感觉还是用字典好

import operator    #或用lambda也可以 
workers = []
w1 = {'姓名':'李泉','工号':120,'工龄':3,'工资':5000}
w2 = {'姓名':'蛙鸣','工号':121,'工龄':4,'工资':5500}
w3 = {'姓名':'响起','工号':122,'工龄':2,'工资':6000}
w4 = {'姓名':'清明','工号':123,'工龄':7,'工资':7000}
w5 = {'姓名':'时节','工号':124,'工龄':5,'工资':8000}
w6 = {'姓名':'雨','工号':125,'工龄':4,'工资':34000}
w7 = {'姓名':'纷纷','工号':126,'工龄':10,'工资':200}
w8 = {'姓名':'路上','工号':127,'工龄':7,'工资':43556}
w9 = {'姓名':'行人','工号':128,'工龄':8,'工资':1234}
w10 = {'姓名':'魂','工号':129,'工龄':9,'工资':87654}

workers.append(w1)
workers.append(w2)
workers.append(w3)
workers.append(w4)
workers.append(w5)
workers.append(w6)
workers.append(w7)
workers.append(w8)
workers.append(w9)
workers.append(w10)

print(sorted(workers,key = operator.itemgetter('工资'),reverse=True))
