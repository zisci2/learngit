# -*- encoding: utf-8 -*-
'''
@File : task7.py
@Time : 2020/03/09 01:24:55
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
7 打印输出9*9乘法表，按照下面的格式：
'''
for i in range(1,10):
    for y in range(1,i+1):
        print(i,"x",y,"=",i*y,"    ",end='')
    print()
  