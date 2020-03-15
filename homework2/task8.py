# -*- encoding: utf-8 -*-
'''
@File : task8.py
@Time : 2020/03/15 12:32:39
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
8  请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
 例如，输入 aaaabbc，输出：a:4
'''

def count(str):
    dict = {} 
    for i in str:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    aa = sorted(dict.items(),key=lambda d:d[1],reverse = True)
    print("该字符串中出现次数的字符如下：")
    print(aa[0][0],":",aa[0][1])
    

print("请输入字符串：")
str = input()
count(str)