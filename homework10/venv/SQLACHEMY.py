#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author：zsw time:2020-5-14

import sys
from sqlalchemy import  Column,String,create_engine,TIMESTAMP,VARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import  datetime

Base = declarative_base()
class Message(Base):
    __tablename__ = 'MESSAGE'
    ID = Column(VARCHAR(20),primary_key=True)
    Name = Column(VARCHAR(40))
    Content = Column(VARCHAR(255))
    Time = Column(TIMESTAMP)
    Is_delete = (int)
engine = create_engine('mysql+mysqlconnector://root:zhong@localhost:3306/homework')


def add(id,name,content):
    DBsession = sessionmaker(engine)
    session = DBsession()
    new_message = Message(ID=id,Name=name,Content=content,Time=datetime.now(),Is_delete=1)
    try:
        session.add(new_message)
        session.commit()
        print("添加成功")
    except Exception as e:
        print("发生错误:",e)
    finally:
        session.close()

add('23','345','4356')
def delete(id):
    DBsession = sessionmaker(engine)
    session = DBsession()
    try:
        session.query(Message).filter_by(ID=id).delete()
        session.commit()
        print("删除成功")
    except Exception as e:
        print("发生错误",e)
    finally:
        session.close()

def update(id,content):
    DBsession = sessionmaker(engine)
    session = DBsession()
    try:
        session.query(Message).filter(Message.ID==id).update({Message.Content:content})
        session.commit()
        print("修改成功")
    except Exception as e:
        print("出现错误",e)
    finally:
        session.close()

def seach(id):
    DBsession = sessionmaker(engine)
    session = DBsession()
    try:
        list = session.query(Message).filter(Message.ID==id).all()
        for i in list:
            print(i.ID,i.Name,i.Content,i.Time)
    except Exception as e:
        print("出现错误",e)
    finally:
        session.close()


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