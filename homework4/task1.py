#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task1.py
@Time : 2020/04/18 13:06:32
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间
；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
    提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
'''

from collections import deque
import time

list = deque("qwertyuiop")
star = time.time()
#print(star)
list.extend("123")
print(list)
list.extendleft("890")
print(list)
end = time.time()
#print(end)
print("程序运行消耗时间为{0:0.4}s".format(end - star))