# -*- encoding: utf-8 -*-
'''
@File : hightfunction.py
@Time : 2020/04/01 08:33:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#定义一个高阶函数, 实现加,减,乘,除计算器功能；
# def jia(a,b):
#     return a+b

# def jian(a,b):
#     return a+b

# def chu(a,b):
#     return a+b

# f = jia(3,4)

# print(f)


def jia(a, b):
    print(a + b)

def jian(a, b):
    print(a - b)

def cheng(a, b):
    print(a * b)

def chu(a, b):
    print(a / b)

if __name__ == '__main__':
    # print("请输入运算式(限两位数+-*/,空格隔开)")
    num1 = int(input("请输入第一个数："))
    a=input("请输入（+-*/):")
    num2 = int(input("请输入第二个数："))
    
    if a=='+':
        print('运算结果为：')
        jia(num1,num2)
    if a=='-':
        print('运算结果为：')
        jian(num1,num2)
    if a=='*':
        print('运算结果为：')
        cheng(num1,num2)
    if a=='%':
        print('运算结果为：')
        chu(num1,num2)