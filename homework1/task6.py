# -*- encoding: utf-8 -*-
'''
@File : task6.py
@Time : 2020/03/09 01:24:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
6  前面2个元素为0，1，输出100以内的斐波那契数列；
'''
a = 0
b = 1
print("前面2个元素为0，1，输出100以内的斐波那契数列如下：")
print(a)
print(b)
while b <= 100:
    print(b)
    a = b
    b = a+b
