#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author：zsw time:2020-6-26

from Crawler import crawler
from multiprocessing import Pool
import threading
from Crawler import SQL

total = 0
def average(list):
    global total
    lock.acquire() #上锁
    if '元/日' in list:
        salary = list.split('元')[0]
        salary = salary.split('-')
        num1 = float(salary[0])*30    #统一以：一个月三十天,工作单位为元/月 记录
        num2 = float(salary[1])*30
        total += (num1+num2)/2
    elif '千/月' in list:
        salary = list.split('千')[0]
        salary = salary.split('-')
        num1 = float(salary[0])*1000
        num2 = float(salary[1])*1000
        total += (num1+num2)/2
    elif '万/月' in list:
        salary = list.split('万')[0]
        salary = salary.split('-')
        num1 = float(salary[0])*10000
        num2 = float(salary[1])*10000
        total += (num1+num2)/2
    elif '万/年' in list:
        salary = list.split('万')[0]
        salary = salary.split('-')
        num1 = float(salary[0])*(10000/12)
        num2 = float(salary[1])*(10000/12)
        total += (num1+num2)/2
    elif list == '':
        total += 0      #还有一些很奇怪的校招，没敢给出工资情况
    else:
        total += 0      #防止出现新奇的工资结算单位，导致系统崩溃

    lock.release()   #释放锁
    threadmax.release()  #释放信号量
    



if __name__ =='__main__':
    print("爬取工资、公司情况...")
    URL = ['https://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
           'https://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',
           'https://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,3.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']
    for url in URL:
        po = Pool(10)   #多进程
        list_text = crawler.get_part(url)
        for text in list_text:
            po.apply_async(crawler.save,(text,))

        print("-----star----")
        po.close()
        po.join()
        print("-----end-----")

    print("开始计算平均工资...")
    aver = 0
    threadmax = threading.BoundedSemaphore(10)    # 限制线程的最大数量为10个
    lock = threading.Lock()   #将锁内代码串行化
    list_salary = SQL.get_salary()
    l = []
    for i in range(len(list_salary)):
        threadmax.acquire()   #增加信号量
        t = threading.Thread(target=average,args=(list_salary[i],))
        t.start()
        l.append(t)
    for t in l:
        t.join()

    aver = total/len(list_salary)
    print("python开发工程师平均薪资为%.2f元/月"%aver)






