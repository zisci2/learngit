# -*- encoding: utf-8 -*-
'''
@File : bibao.py
@Time : 2020/04/03 08:39:00
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

''''
练习1
利用闭包返回一个计数器函数，每次调用它返回递增整数：
# -*- coding: utf-8 -*-

# 测试:
******

'''


# def createCounter():  
#     i = [0]
#     def Add():
        
#         i[0] = i[0]+1 
#         return i[0]
#     return Add

# #方法二  
# i = 0
# def createCounter():  
#     def Add():
#         global i
#         i = i+1 
#         return i
#     return Add
# #这种方法i会一直累加，之前失败的原因是，我不用return而是用了print
    

# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')


############################################################################################


import time

def play_time(function):
    def aa():
        t1 = time.time()
        function()
        t2 = time.time()
        print(t2-t1,"秒")
    return aa

@play_time
def jia():
    a = 0
    for i in range(1,100):
        a = a+i
    print(a)




jia()