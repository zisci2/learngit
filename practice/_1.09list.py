#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : _1.09list.py
@Time : 2020/02/28 20:22:49
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#定义一个集合类型的变量(用2种方法初始化),然后进行相应的 元素的操作;
a = {'q','w','e','r'}
print(a)
a.add('aa')
a.remove('q')
print(a)
b = set('mmm')
print(b)
b.add('uu')
b.update('oo')
b.discard('uu')
print(b)