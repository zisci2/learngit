#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task2.py
@Time : 2020/04/18 13:07:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？ 
 将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；
'''
import datetime

# today = datetime.datetime.now()
# print(today)

def get_week(date):
    week_day = {0:"星期一",1:"星期二",2:"星期三",3:"星期四",4:"星期五",5:"星期六",6:"星期日"}
    day = datetime.date.weekday(date)
    return week_day[day]

def WEEK():
    year =input("请输入年份：")
    month =input("请输入月份：")
    day =input("请输入具体号数：")
    date = year+"-"+month+"-"+day
    # date = '2020-4-18'
    date1 = datetime.datetime.strptime(date,'%Y-%m-%d')
    print(date,"是",get_week(date1))


def school_week(num):
    star = datetime.date(2020,2,17)
    delta1 =datetime.timedelta((num-1)*7)
    day1 = star + delta1
    delta2 = datetime.timedelta(num*7-1) 
    day2 = star + delta2
    print("第{0}周的日期为{1} ~ {2}".format(num,day1,day2))

# print(datetime.date(2020,4,18)-datetime.timedelta((3-1)*10))
# school_week(3)

def main():
    num = int(input("想查询日期为周几请输入1，想查询华电第几周为几号请输入2："))
    if num == 1:
        WEEK()
    if num == 2:
        num1 = int(input("请问你想查询第几周？全部请输入00:"))
        if num1 == 00:
            for i in range(1,28):
                school_week(i)
        else:
             school_week(num1)


main()