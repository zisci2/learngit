# -*- encoding: utf-8 -*-
'''
@File : task10.py
@Time : 2020/03/15 15:35:12
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
10 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
'''

def calculate(a,b,str):
    if str is '+':
        return a+b
    if str is '-':
        return a-b
    if str is '*':
        return a*b
    if str is '/':
        return a/b

a = int(input("输入第一个数："))
str = input("输入运算符：")
b = int(input("输入二个数："))
print("运算结果为：",calculate(a,b,str))