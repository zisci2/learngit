# -*- encoding: utf-8 -*-
'''
@File : task7.py
@Time : 2020/04/07 20:03:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
7 对一篇中文文献, ;利用jieba库,进行词频统计分析找出文章的关键词(取词频最高的前10个词语,作为文章的关键字);
  
'''

import jieba

def getText():
    txt = open(r"E:\Python\CodeProjects\PythonProjects\opms\homework3\冬牧场节选.txt",'r',encoding="utf-8").read()
    for ch in '~!@#$%^&*()_+=-`<>?:"|\';,./，。 ... …？！\n（）':
        txt = txt.replace(ch,"")
    return txt

def stat():
    totall = {}
    words = []
    all = jieba.lcut(getText())
    #去除单个字
    for word in all:
        if len(word) == 1:
            continue
        else:
            words.append(word)
    #print(words)
    for i in words:
        if i in totall:
            totall[i] += 1
        else:
            totall[i] = 1
    _totall = sorted(totall.items(),key=lambda d: d[1],reverse=True)
    print("文章的关键词如下：")
    count = 0
    for key,value in _totall:
        count +=1
        print(key," ",value)
        if count>=10:
            break;

stat()