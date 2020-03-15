# -*- encoding: utf-8 -*-
'''
@File : task7.py
@Time : 2020/03/15 12:12:11
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
    A---成绩>=90;  
    B-->成绩在 [80,90)
    C-->成绩在 [70,80)
    D-->成绩<70

'''

import random
def judge(list):
    list1 = []
    for i in list:
        if i >= 90:
            list1.append('A')
        if i >=80 and i < 90:
            list1.append('B')
        if i >=70 and i < 80:
            list1.append('C')    
        if i <70:
                list1.append('D')    
    return list1 
           
list = [random.randint(0,100) for _ in range(1,11)]
list1 = judge(list)
print("学生成绩及等级如下：")
for i in range(0,len(list)):
    print(list[i],"  ",list1[i])