#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author：zsw time:2020-5-14
'''
2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）
（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
   使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；
'''

# import pymysql
#
# db = pymysql.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'zhong',
#     database = 'homework' )
#
# cursor = db.cursor()
# #增
# sql = 'insert into MESSAGE (ID,Content,Name) values(%s,%s,%s)'
# mm = [('1','新冠病毒','张三'),
# ('2','美国','王大'),
# ('3','开学','王二'),
# ('4','考试','王三'),
# ('5','线上','王四'),
# ('6','口罩','王五'),
# ('7','疫苗','王六'),
# ('8','雷课堂','王七'),
# ('9','python','王八'),
# ('10','java','王九'),
# ('11','C语言','王十')]
# #执行
# cursor.executemany(sql,mm)
# #提交
# db.commit()
# print(cursor.rowcount,"条信息更新成功")
#
# #删
# sql = 'delete from MESSAGE where ID = "10" '
# cursor.execute(sql)
# db.commit()
# print("ID为1的用户信息删除成功")
'''那是否删除的字段有啥用呢'''
#
# #改
# sql = 'update MESSAGE  set Name="伍六七" where Name = "张三" '   ##为什么需要用“”而‘’不行
# cursor.execute(sql)
# db.commit()
# print(cursor.rowcount,"条记录修改成功")
#
# #改
# sql = 'update MESSAGE  set Name="伍六七" where Name = "张三" '   ##为什么需要用“”而‘’不行
# cursor.execute(sql)
# db.commit()
# print(cursor.rowcount,"条记录修改成功")
#
# #查
# sql = 'select name from MESSAGE'
# cursor.execute(sql)
# for i in cursor.fetchall():
#     print(i)
#
# db.close()


import pymysql,sys

def add(id,name,content):
    db = pymysql.connect('localhost','root','zhong','homework')
    cursor = db.cursor()
    sql = "insert into MESSAGE (ID,Content,Name) values(%s,%s,%s)"
    #若直接将数值写入，SQL则非得"或''' 双引号里面的字段会经过编译器解释然后再当作HTML代码输出，但是单引号里面的不需要解释，直接输出
    #print(insert into MESSAGE (ID,Content,Name) values(id,content,name))
    # print(sql%(id,content,name))
    try:
        cursor.execute(sql,(id,content,name))
        db.commit()
        print("添加成功")
    except Exception as e:
        print("发生错误:",e)
    finally:
        db.close()

def delete(id):
    db = pymysql.connect('localhost','root','zhong','homework')
    cursor = db.cursor()
    sql = "update MESSAGE set Is_delete = 1 where ID = %s "
    try:
        cursor.execute(sql,id)
        db.commit()
        print("删除成功")
    except Exception as e:
        print("发生错误",e)
    finally:
        db.close()

def update(id,content):
    db = pymysql.connect('localhost','root','zhong','homework')
    cursor = db.cursor()
    sql = 'update MESSAGE set Content = %s where ID = %s'
    try:
        cursor.execute(sql,(content,id))
        db.commit()
        print("修改成功")
    except Exception as e:
        print("出现错误",e)
    finally:
        db.close()

def seach(id):
    db = pymysql.connect('localhost','root','zhong','homework')
    cursor = db.cursor()
    sql = 'select * from MESSAGE where ID = %s'
    # print(sql%id)
    try:
        cursor.execute(sql,id)
        for i in cursor.fetchall():
            print(i)
    except Exception as e:
        print("出现错误",e)
    finally:
        db.close()

if __name__ == '__main__':
    print("****1.添加信息****")
    print("****2.删除信息****")
    print("****3.修改信息****")
    print("****4.查询信息****")
    print("*****0.退出******")
    while True:
        num = input("请选择：")
        if num == '1':
            id = input("请输入ID:")
            name = input("请输入姓名：")
            content = input("请输入内容：")
            add(id,name,content)
        elif num == '2':
            id = input("请输入需删除者的id：")
            delete(id)
        elif num == '3':
            id = input("请输入需修改者的ID：")
            content = input("请输入修改内容：")
            update(id,content)
        elif num == '4':
            id = input("请输入需查询者ID：")
            seach(id)
        else:
           sys.exit()
