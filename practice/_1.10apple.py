# -*- encoding: utf-8 -*-
'''
@File : test1.py
@Time : 2020/03/08 11:44:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#提示输入需要购买的苹果的重量(斤),然后提示输入每斤的价格,请计算应支付的总价,并打印提示输出;

a=int(input('请输入想要购买的苹果斤数：'))  
b=int(input('请输入苹果的单价：'))
c=a*b
print('您购物的总价为：',c)