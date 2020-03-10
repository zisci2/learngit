# -*- encoding: utf-8 -*-
'''
@File : task3.py
@Time : 2020/03/08 21:50:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
3 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；
'''

list1 = [122,34,67,8,90]
list2 = [122,354,657,890,789]
list3 = [x for x in list1 if x in list2]
print("这两个列表中的相同元素有：",list3)