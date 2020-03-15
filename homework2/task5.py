# -*- encoding: utf-8 -*-
'''
@File : task5.py
@Time : 2020/03/15 11:06:18
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
5  写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
'''


def judge(dic):
    aa = {}
    for key,value in dic.items():
        if len(value) > 2:
            aa[key] = value[0:2]
        else:
            aa[key] = value
    return aa

dic = {"k1":"werty","k2":'1324',"k3":[2134,12435,13245,12345]}   #int无长度
print("原字典如下：")
print(dic)
print("新字典如下：")
print(judge(dic))
