# -*- encoding: utf-8 -*-
'''
@File : tsak2.py
@Time : 2020/03/15 10:01:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
2 编写一个函数,接收n个数字，求这些参数数字的和;
'''

def sum(n):
    b = 0
    while n != 0:
        print("请输入倒数第",n,"个数据：")
        aa = int(input())
        n = n-1
        b = b+aa
    print("输入数据之和为：",b)
    
n = int(input("请问你想求几个数据的和？"))
sum(n)