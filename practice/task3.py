#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task3.py
@Time : 2020/04/24 00:15:13
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
三、定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
'''

class dictclass(object):
    def __init__(self,dict):
        self.dict = dict

    def del_dict(self,key):
        self.dict = {k:self.dict[key] for k in self.dict.keys()-{key}} #自己之前没有用过，留意
        return self.dict

    def get_dict(self,key):
        if key in self.dict:  #区别dict.items()
            return self.dict[key]
        else:
            print("not found")

    def get_key(self):
        return self.dict.keys()

    def update_dict(self,dict1):
        dict2 = self.dict.copy()
        dict2.update(dict1)
        list = dict2.keys()
        return list

dict = {'i':10,'love':20,'you':30}
A = dictclass(dict)
#删除key
key1 = 'you'
print(A.del_dict(key1))
#判断key
key2 = 'i'
print("dict['{}']的对应值为{}".format(key2,A.get_dict(key2)))
#返回键
print(A.get_key())
#合并
dict1 = {'python':20}
print(A.update_dict(dict1))