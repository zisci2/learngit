#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author：zsw time:2020-6-26

import pymysql

#将公司名称、工资的内容加入数据库
def Add(list):
    db = pymysql.connect('localhost','root','zhong','Spider')
    cursor = db.cursor()
    sql = 'insert into `job_data`(company,address,salary,date) values(%s,%s,%s,%s)'
    try:
        cursor.execute(sql,(list[0],list[1],list[2],list[3]))
        db.commit()
        print("添加成功")
    except Exception as e:
        print("数据加入数据错误：",e)
    finally:
        db.close()

#从数据库取出工资数据
def get_salary():
    db = pymysql.connect('localhost','root','zhong','Spider')
    cursor = db.cursor()
    sql = 'select salary from job_data '
    try:
        cursor.execute(sql)
        list = []
        for i in cursor.fetchall():
            list.append(i[0])
        return list
    except Exception as e:
        print("数据查询出现错误",e)
    finally:
        db.close()
