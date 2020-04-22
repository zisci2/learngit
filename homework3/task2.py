# -*- encoding: utf-8 -*-
'''
@File : task2.py
@Time : 2020/03/24 17:56:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx
'''

import os


os.system('cls')
def Read():
    list = []
    try:
        f = open("E:\桌面\input.txt","r",encoding="utf8")
        while True:
            a = f.readline()
            if not a:
                return list
            list.append(a)
    except EOFError:
        print("文件读取出现问题！")
    finally:
        f.close()

'''阿拉伯数字转换成汉字数字'''
# def change(num):
    
i = 0
for line in Read():
    i = i+1
    print("#第{}行：{}".format(i,line))
    #print("第%s行：%s" %(i,line))
