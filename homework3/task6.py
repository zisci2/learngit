# -*- encoding: utf-8 -*-
'''
@File : task6.py
@Time : 2020/04/07 20:02:41
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
6  对一篇英文小说，进行词频统计，输出前20个出现频率最高的单词；
        英文小说"老人与海"     链接：https://pan.baidu.com/s/1goqK3zF8VBUFuD_2ezfZ7Q   提取码：mv04 
    提示：
    1 可以先定义一个函数，专门来处理英文文章的读取问题；读取时，解决大小写问题，以及标点符号问题（如，将标点符号都替换成空格）；
'''
import os

def getText():
    txt  =open(r"E:\Python\CodeProjects\PythonProjects\opms\homework3\海明威.txt",encoding="utf-8").read()
    txt = txt.lower()  #全变成小写
    for ch in '?/!"@#$%^&*()+-:<>,"“”.;\|.`~':
        txt = txt.replace(ch," ")
    return txt

def sta():
    totall = {}
    str = getText().split()
   # print(str)
    for i in str:
        if i in totall:
            totall[i] +=1
        else:
            totall[i] = 1
    _totall = sorted(totall.items(),key=lambda d : d[1],reverse=True) #_totall是列表，不可像遍历字典一样，写成for key,value in sort_d.items()
    print("前20出现频率最高的单词如下：")
    count = 0
    for key,value in _totall:
        count +=1
        print(key,"  ",value)
        if count>=20:
           # print("**************%d"%count)
            break;

    #print(_totall[10])

sta()

