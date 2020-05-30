#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task1.py
@Time : 2020/05/23 18:03:55
@Author : xdbcb8
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
1  有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现
'''
from multiprocessing  import  Pool
import random,os,time

def score(num):
    for i in num:
        print("线程{}--{}".format(os.getpid(),i))
        time.sleep(0.3)

if __name__ == '__main__':
    pool = Pool(5)
    num = [random.randint(0,100) for i in range(100)]
    pool.apply_async(score,(num[0:20],))
    pool.apply_async(score,(num[20:40],))
    pool.apply_async(score,(num[40:60],))
    pool.apply_async(score,(num[60:80],))
    pool.apply_async(score,(num[80:100],))

    print("----开始记录---")
    pool.close()
    pool.join()
    print("----完事收工---")
