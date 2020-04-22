# -*- encoding: utf-8 -*-
'''
@File : task3.py
@Time : 2020/04/07 19:50:21
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
3 编写一个程序，读取文件中保存的10个学生成绩名单信息
(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
'''

import os,operator

studens = []
try:
    f = open("E:\桌面\input.txt","r",encoding="utf-8")
   
    for a in f.readlines():
        a = a.split(" ")
        studen = {}
        studen['id'] = a[0]
        studen['name'] = a[1]
        studen['score'] = int(a[2])
        studens.append(studen)
except EOFError:
    print("文件读取有问题")
else:
    f.close()

print(studens)
a = sorted(studens,key=operator.itemgetter("score"),reverse=True)
print("成绩从高到低排序如下：")
for i in a:
    print(i["id"],"  ",i["name"],"  ",i["score"])
