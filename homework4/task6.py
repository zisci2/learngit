#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task6.py
@Time : 2020/04/18 13:10:53
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
    名称         日期                   类型（文件夹或者 文件）       大小

效果如：

'''
import os 
from datetime import datetime

def judge(path):
    list = [('名称','修改日期','类型','大小')]
    if os.path.isdir(path):
        path_list = os.listdir(path)
        for i in path_list:
            if os.path.isdir(i):#突然发现，这里不用join都行？相对路径吗，好像也不对啊就一个文件名
                name = os.path.basename(i)
                time = datetime.fromtimestamp(int(os.path.getmtime(i)))
                Type = "文件夹"
                size = " "
                list.append((name,time,Type,size))
            else:
                name = os.path.basename(i)
                time = datetime.fromtimestamp(int(os.path.getmtime(i)))
                Type = "文件"
                size = str(os.path.getsize(path)/1024)+"kb"
                list.append((name,time,Type,size))


    if os.path.isfile(path):
        name = os.path.basename(path)
        time = datetime.fromtimestamp(int(os.path.getmtime(path)))
        Type = "文件"
        size = os.path.getsize(path)/1024+"kb"
        list.append((name,time,Type,size))
    if os.path.isfile(path):
        print("找不到该地址！")    #不知道为什么如果用来else，不管文件存不存在，else语句都会打印？？？！！！！
    return list


path = "E:\Python\CodeProjects\PythonProjects\opms"
# print(os.path.basename(path))
# print(os.path.getmtime(path))#时间戳
# print(datetime.fromtimestamp(int(os.path.getmtime(path))))
# print(os.path.getsize(path)/1024)#kb

# for i in judge(path):
#     print(i)

tplt = "{0:{4}^10}\t{1:}\t{2:{4}^30}\t{3:^10}"
for i in judge(path):
    print(tplt.format(i[0],i[1],i[2],i[3],' '))