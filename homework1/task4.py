# -*- encoding: utf-8 -*-
'''
@File : task4.py
@Time : 2020/03/09 01:23:21
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
4. 判断用户输入的年份是否为闰年
'''

year = int(input("请输入查询的年份："))
if year%4 == 0 and year%100 != 0:
    print(year,"是普通闰年")
if year%400 == 0:
    print(year,"是世纪闰年")
else:
    print(year,"不是闰年")