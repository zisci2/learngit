#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task1.py
@Time : 2020/04/24 00:14:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
       实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
'''

class dog():
       dog_list = [{'color':'black','count':50,'price':'50 RMb'},
       {'color':'white','count':40,'price':'60 RMb'},
       {'color':'yellow','count':30,'price':'70 RMb'}]

       ##需要输入数据的函数
       # def sell(self):
       #        color = input("请输入想卖的狗的颜色：")
       #        mark = 0
       #        for i in self.dog_list:
       #               if i['color'] != color:
       #                      mark +=1
       #                      continue
       #               else:
       #                      num = int(input("请输入想卖的狗的数量："))
       #                      if i['count'] < num:
       #                             print("数量太多了，小店不够")
       #                             continue
                                   
       #                      else:
       #                             i['count'] -= num
       #        if mark ==len(self.dog_list):
       #               print("没有这种颜色的狗子，您好在不送嘞")       
       #        ##一定要注意循环的情况，作业4登录作业的时候还没发现这么简单的问题

       #不想输入数据下用的函数
       def sell(self):
              print("每种颜色的狗卖出去13只")
              for i in self.dog_list:
                     i['count'] -= 13

       def buy(self):
              print("每种颜色的狗补充10只")
              for i in self.dog_list:
                     i['count'] += 10

t = dog()
t.sell()
t.sell()
t.sell()
print()
t.buy()
print()
print("经过一番激烈的买卖，狗子们还剩下：")
for i in t.dog_list:
       print("{}   {}只".format(i['color'],i['count']))