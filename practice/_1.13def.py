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

# def apple(a,s):
#     return a*s
# price = int(input("请输入苹果价格"))
# num = int(input("请输入苹果重量："))
# print("应付款{}元".format(apple(price,num)))


#使用不定长参数定义一个函数;
# 实现对输入数据的封装(封装成一个列表和字典),然后打印输出;
# def fun(x,**args):
#     print("列表为：",x)
#     print("字典为：",args)
# fun(1, a=2,b=3)



#定义一个函数,  打印输出列表里面的元素;  然后增加列表中的元素, 然后再输出新的列表;

# 主程序中,打印这个列表的地址(传参之前,传参之后);
# def change(b):
#     print("重新赋值之前的地址：",id(b))
#     b=10
#     print("重新赋值之后的值：",b)
#     print("重新赋值之后的地址：",id(b))

# c=2
# print("c的地址：",id(c))
# change(c)
# print("传了参数之后c的地址：",id(c))
# print("c的值：",c)



#初始化一个列表(1-20之间的整数) ;
# 然后 使用匿名函数,列表解析式, 来打印输出一个列表中的奇数;
def shu(list1):
    res=filter(lambda x:x%2!=0,list1)  #返回奇数
    print(list(res))
l=list(range(1,20))
shu(l)