# -*- encoding: utf-8 -*-
'''
@File : task9.py
@Time : 2020/03/15 15:21:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
9  定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
'''
import random
def Sort(list):
    list.sort()    #!!!! aa=list.sort()是不行的，sort没有返回值
   # print(list)
    return list

list = [random.randint(0,90) for _ in range(0,10)]
print("原数组为：")
print(list)
aa = Sort(list)
print("排序后的数组为：")
print(aa)