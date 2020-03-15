# -*- encoding: utf-8 -*-
'''
@File : task6.py
@Time : 2020/03/15 11:58:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
6  定义一个函数, 打印输出n以内的斐波那契数列;
'''
def number(n):
    a , b = 0,1
    print(n,"以内的裴波那契数如下：")
    if a < n :
        print(a)
    if b < n:
        print(b)
    while b <= n:
        print(b)
        a = b
        b = a + b 
        

n = int(input("请输入裴波那契数的上限值："))
number(n)