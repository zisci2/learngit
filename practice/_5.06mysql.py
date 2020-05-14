#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : _5.06mysql.py
@Time : 2020/05/06 09:39:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
练习二：
   创建一个留言板的表（ID，留言主题，留言人，留言时间）4个字段，
   注意，字段请用英文；
   完成对这个表记录的增，删，改，查询；
   用PyMySQL驱动方式
'''

# import mysql.connector

# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'zhong',
#     database = 'test'
# )

# # try:
# #     mycursor = mydb.cursor()
# #     #创建留言表
# #     sql1 = '''creat table message (ID varchar(50),theme varchar(20),
# #             time datetime)'''
# # except Exception as e:
# #     print("数据库操作出现问题",e)
# # finally:
# #     mydb.close()

# mycursor = mydb.cursor()
# #创建留言表
# sql1 = '''create table message (ID varchar(50),theme varchar(20),name varchar(20),
#         time varchar(50))'''
# mycursor.execute(sql1)
# print("message表创建成功！")

# #增
# sql = 'insert into message(id,theme,name,time) values(%s,%s,%s,%s)'
# mm = [('1','新冠病毒','张三','2020-02-01'),
# ('2','美国','王大','2020-02-01'),
# ('3','开学','王二','2020-02-02'),
# ('4','考试','王三','2020-02-03'),
# ('5','线上','王四','2020-02-04'),
# ('6','口罩','王五','2020-02-05'),
# ('7','疫苗','王六','2020-02-06'),
# ('8','雷课堂','王七','2020-02-07'),
# ('9','python','王八','2020-02-08'),
# ('10','java','王九','2020-02-09'),
# ('11','C语言','王十','2020-02-10')]
# #执行
# mycursor.executemany(sql,mm)
# #提交
# mydb.commit()
# print(mycursor.rowcount,"条信息更新成功")

# #删
# sql = 'delete from message where id = "10" '
# mycursor.execute(sql)
# mydb.commit()
# print("ID为1的用户信息删除成功")

# #改
# sql = 'update message  set name="伍六七" where name = "张三" '   ##为什么需要用“”而‘’不行
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"条记录修改成功")

# #查
# sql = 'select name from message'
# mycursor.execute(sql)
# for i in mycursor.fetchall():
#     print(i)
 
# mydb.close()



""" 使用MYSQL """
import pymysql

db = pymysql.connect(host = 'localhost',user = 'root',password = 'zhong',database = 'test' )

#创建
cursor = db.cursor()
cursor.execute("drop table if exists message")  #执行的时候回自动转换为大写，想提高效率可直接用大写
sql1 = '''create table message (ID varchar(50),theme varchar(20),name varchar(20),
        time varchar(50))'''
cursor.execute(sql1)
print("message表创建成功！")

#增
sql = 'insert into message(id,theme,name,time) values(%s,%s,%s,%s)'
mm = [('1','新冠病毒','张三','2020-02-01'),
('2','美国','王大','2020-02-01'),
('3','开学','王二','2020-02-02'),
('4','考试','王三','2020-02-03'),
('5','线上','王四','2020-02-04'),
('6','口罩','王五','2020-02-05'),
('7','疫苗','王六','2020-02-06'),
('8','雷课堂','王七','2020-02-07'),
('9','python','王八','2020-02-08'),
('10','java','王九','2020-02-09'),
('11','C语言','王十','2020-02-10')]
#执行
cursor.executemany(sql,mm)
#提交
db.commit()
print(cursor.rowcount,"条信息更新成功")

#删
sql = 'delete from message where id = "10" '
cursor.execute(sql)
db.commit()
print("ID为1的用户信息删除成功")

#改
sql = 'update message  set name="伍六七" where name = "张三" '   ##为什么需要用“”而‘’不行
cursor.execute(sql)
db.commit()
print(cursor.rowcount,"条记录修改成功")

#改
sql = 'update message  set name="伍六七" where name = "张三" '   ##为什么需要用“”而‘’不行
cursor.execute(sql)
db.commit()
print(cursor.rowcount,"条记录修改成功")

#查
sql = 'select name from message'
cursor.execute(sql)
for i in cursor.fetchall():
    print(i)

db.close()