#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author：zsw time:2020-6-24

import pymysql

#添加内容（该企业的产品及服务信息）到数据库
def Add(text,id):
    db = pymysql.connect('localhost','root','zhong','crawler')
    cursor = db.cursor()
    sql = 'update temp_icp_web2 set message = %s where autoID = %s '
    try:
        cursor.execute(sql,(text,id))
        db.commit()
        print("添加成功")
    except Exception as e:
        print("数据加入数据错误：",e)
    finally:
        db.close()

#从数据库取出网址
def get_url(id):
    db = pymysql.connect('localhost','root','zhong','crawler')
    cursor = db.cursor()
    sql = 'select web_url from temp_icp_web2 where autoID = %s'
    try:
        cursor.execute(sql,id)
        for i in cursor.fetchall():  #从元组中去元组
            url = "".join(tuple(i))  #将tuple转换成string类型后才能分割
            url = url.split(";")
            return url
    except Exception as e:
        print("数据查询出现错误",e)
    finally:
        db.close()
