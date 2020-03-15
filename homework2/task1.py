# -*- encoding: utf-8 -*-
'''
@File : task1.py
@Time : 2020/03/11 13:41:11
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
1 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
'''
def judge (str):
    print("数据的长度为：",len(str))

str = eval(input("请输入想知道长度的数据："))
judge(str)
