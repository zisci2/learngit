# -*- encoding: utf-8 -*-
'''
@File : task5.py
@Time : 2020/03/09 01:23:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
5  使用random模块，生成随机数，来初始化一个列表，元组；
     使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；
'''
import random
list  = random.sample(range(0,100),10)
tup = tuple(random.sample(range(0,2000),15))
print(list)
print(tup)