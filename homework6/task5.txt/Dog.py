#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : dog.py
@Time : 2020/04/25 14:37:46
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

class dog(object):
    blood = 80
    attack = 15
    def __init__(self,name):
        self.name = name
    def be_attacked(self,num):
        self.blood -= 10
        self.attack -= num
        if self.attack <=0:
            self.attack = 0