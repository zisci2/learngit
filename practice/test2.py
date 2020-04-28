# -*- encoding: utf-8 -*-
'''
@File : test2.py
@Time : 2020/03/08 11:47:18
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

for n in range(2,10):
    for x in range(2,n):
        if n %x == 0:
            print(n,'等于', x,'*',n/x)
            break
        else:
            print(n,'是质数')