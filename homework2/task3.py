# -*- encoding: utf-8 -*-
'''
@File : tsak3.py
@Time : 2020/03/15 10:36:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
   数字列表请用随机数函数生成;
'''

import random
def choice(list):
    print("列表中的奇数如下：")
    for i in list:
        if i%2 != 0:
            print(i)

list = [random.randint(0,1000) for _ in range(1,11)]
print("产生的列表如下：")
print(list)
choice(list)