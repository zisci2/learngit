#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task3.py
@Time : 2020/05/23 18:05:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
3  多进程练习：
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
'''
import time
from multiprocessing import Pool

def prime(num):
    if num == 1 or num==2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def not_use():
    num = 0
    start = time.time()
    for i in range(1,100001):
        if(prime(i)):
            num += 1
    end = time.time()
    print("不使用多线程耗时{:.4}，统计素数{}个".format(end-start,num))

def use(pool_num):
    num = 0
    start = time.time()
    pool = Pool(pool_num)
    for i in range(1,100001):
        s = pool.apply_async(prime,(i,))
        if(s.get()):  #还需要获取返回值
            num +=1
    pool.close()
    pool.join()  #好像非必须
    end = time.time()
    print("使用{}个线程耗时{:.4}，统计素数{}个".format(pool_num,end-start,num))

if __name__ == "__main__":
    print("开始计算...")
    not_use()
    use(4)
    use(10)
    print("计算结束...")