# -*- encoding: utf-8 -*-
'''
@File : task5.py
@Time : 2020/04/07 20:01:41
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
5文件编程小项目

How many roads must a man walk down
Before they call him a man
How many seas must a while dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind 
The answer is blowing in the wind
'''



import os

def Read():
    list = []
    try:
        f = open("E:\桌面\Blowing in the wind.txt",'r',encoding="utf-8")
        while True:
            a = f.readline()
            if not a:
                return list;
            list.append(a)
    except EOFError:
        print("原文件文件读取出现问题！")
    finally:
        f.close()

def _input():
    try:
        list = []
        for line in Read():
            list.append(line)
        i = len(list)
        ff = open("E:\桌面\Blowing in the wind.txt","w")
        ###为什么加一个    if “Blowin' in the wind” not in list[0]：就不行了呢？？？？？？？？？
        list.insert(0,"Blowin' in the wind\n")
        list.insert(1,"Bob Dylan\n")
        list.insert(i+2,"\n   1962 by Warner Bros.lnc\n")
        for line in list:
            ff.write(line)
    except EOFError:
        print("文件读取有问题！")
    finally:
        ff.close()

def main():
    _input()
    for line in Read():
        print(line,end="")


main()
# for line in Read():
#     print(line,end="")
