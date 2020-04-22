#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task9.py
@Time : 2020/04/18 13:08:46
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
9 从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块）
'''

import os
import requests

def download(address):
    url1 = requests.get(address)
    url2 = url1.content  #返回二进制
    # path = "E:\Python\CodeProjects\PythonProjects\opms\homework4\%s.jpg"%(address[1])    #无法成功
    path = "E:\Python\CodeProjects\PythonProjects\opms\homework4\\"+address.split("/")[-1]
    print(path)
    with open(path,"wb") as f:
       f.write(url2)
    print("下载成功！")

if __name__=="__main__":
    address = "https://img01.sogoucdn.com/app/a/100520093/e18d20c94006dfe0-feec70b0eb485633-231428f5bb1f4a14f5aa7c5040db29aa.jpg"
    download(address)
