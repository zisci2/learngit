#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : people.py
@Time : 2020/04/25 14:38:07
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

class people(object):
    blood = 100
    attack = 10
    def __init__(self,name):
        self.name = name
    def be_attacked(self,num):
        self.blood -= 15
        self.attack -= 2
        if self.attack <= 0:
            self.attack = 0

