# -*- encoding: utf-8 -*-
'''
@File : task8.py
@Time : 2020/04/07 20:04:12
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
8 在2个文件中存放了 英文 计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 
请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
    比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
'''

import os 

def getText(str):
    txt = open(str,'r',encoding='utf-8').read()
    txt = txt.lower()
    for ch in '~!@#$%^&*()_+=--`|\;:/.,<>/“"”':
        txt = txt.replace(ch," ")
    return txt

def stat(str):
    totall = {}
    words = []
    all = getText(str).split() 
    for word in all:
        if len(word) == 1 :
            continue
        if word in {'is','on','of','the','and','my','you','to','it','in','be','for','not','that','his'
        ,'he','are','was','were','she','no'}:#去掉一些常用介词，人称等无用词汇
            continue
        else:
            words.append(word)

    for i in words:
        if i in totall:
            totall[i] += 1
        else:
            totall[i] = 1
    _totall = sorted(totall.items(),key=lambda d: d[1],reverse=True)

    top = []
    for i in range(10):
        top.append(_totall[i])

    return top


str1 = input("请输入第一篇文章地址：")
str2 = input("请输入第二篇文章地址：")
# str1='E:\Python\CodeProjects\PythonProjects\opms\homework3\傲慢与偏见.txt'
# str2='E:\Python\CodeProjects\PythonProjects\opms\homework3\海明威.txt'
i = 0
for word1 in stat(str1):
    for word2 in stat(str2):
        if word1[0] in word2[0]:
            i +=1
        

print("两篇文章相似度为{}%".format((i*10)))
# print(stat(str1))
# print(stat(str2))