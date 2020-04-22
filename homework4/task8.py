#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task8.py
@Time : 2020/04/18 13:08:10
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
8 京东二面笔试题
1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
'''

import os
import random

def creat_ip():
    i = random.randint(1,254)
    return '172.25.254.'+str(i)

def creat_file():
    with open(r"E:\Python\CodeProjects\PythonProjects\opms\homework4\ip.txt","w+",encoding="utf-8") as f:
        for i in range(0,1200):
            f.write(creat_ip()+'\n')

def main():
    totall = {}
    with open(r"E:\Python\CodeProjects\PythonProjects\opms\homework4\ip.txt","r",encoding="utf-8")as f:
        for line in f:
            c=line.strip("\n")
            # a = line.replace("."," ")
            b = c.split(".")
            for i in b:
                if i in totall:
                    totall[i] += 1
                else:
                    totall[i] = 1
    return totall

if __name__=="__main__":
    # creat_file()
    totall = sorted(main().items(),key=lambda k: k[1],reverse=True)
    count = 0
    print("出现前十的IP如下：")
    for j in totall:
        count +=1
        print("172.25.254.{}".format(j[0]))
        if count >=9:
            break
