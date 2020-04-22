# -*- encoding: utf-8 -*-
'''
@File : task4.py
@Time : 2020/04/07 20:00:59
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''

4 题目要求：
 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
 将当前img目录所有以.png结尾的后缀名改为.jpg.
'''

import random
import string
import os

def gen_code(len=4):
    li = random.sample(string.ascii_letters+string.digits,len)
    #print(li)
    return ''.join(li)    #返回通过指定字符连接序列中元素后生成的新字符串。

def creat_file():
    #生产多个文件名
    li = {gen_code() for i in range(10)}
    os.mkdir('img')
    for name in li:
        str = os.path.realpath('img')+'\\'+name+'.png'
        # print(os.path.realpath('img')+'\\')
        # print(str)
        open(str,"a")

# creat_file()

def modifiy(dirname,old,new):
    if os.path.exists(dirname):
        pngfile = [filename for filename in os.listdir(dirname)
        if filename.endswith(old)]

        fname = [os.path.splitext(filename)[0]
        for filename in pngfile]

        for filename in fname:
            old = os.path.join(dirname,filename+old)
            new = os.path.join(dirname,filename+new)
            try:
                os.rename(old,new)
            except FileNotFoundError:
                pass
            

    else:
        print("重命名失败，文件还没创建")
        creat_file()


i = 0
while i<10:
    i =i+1
    modifiy('img','.png','.jpg')
    if i==10:
        print("重命名成功")