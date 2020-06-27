#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author：zsw time:2020-6-26

import re,requests
from bs4 import BeautifulSoup
from Crawler import SQL


#爬取网页
def getHtmlText(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}
        #伪装成浏览器
        res = requests.get(url,headers=headers,timeout=10)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except requests.HTTPError as e:  #抓取状态错误
        print(e)
        print('抓取状态错误')
        return "404"
    except Exception as e:  #抓取其他错误
        print(e)
        print('抓取的其他错误')
        return "404"

#将网页数据分成小份
def get_part(url):
    h_text = getHtmlText(url)
    if h_text == "404":
        return "404"
    else:
        list = []
        soup = BeautifulSoup(h_text,'html.parser')
        for i in soup.find_all('div',class_="el"):
            i = str(i)
            if '<span class="t2">' in i and '<div class="el title">' not in i:  #过滤掉一些不合格的检索结果
                list.append(i)
        return list


#解析数据,得到信息列表
def get_data(text):
    #创建正则表达式对象，表示规则
    findcompany = re.compile(r'target="_blank" title="(.*?)">')   #公司名称
    findsite = re.compile(r'<span class="t3">(.*?)</span>')       #工作地区
    findsalary = re.compile(r'<span class="t4">(.*?)</span>')     #工资
    finddate = re.compile(r'<span class="t5">(.*?)</span>')       #发布信息日期
    data = []
    if '<span class="t2">' in text and '<div class="el title">' not in text:
        company = re.findall(findcompany, text)[1]
        data.append(company)
        site = re.findall(findsite,text)[0]
        data.append(site)
        salary = re.findall(findsalary, text)[0]
        data.append(salary)
        date = re.findall(finddate,text)[0]
        data.append(date)
        return data
    else:
        return "None"


#保存信息到数据库
def save(text):
    if get_data(text) == 'None':
        pass
    else:
        list = get_data(text)
        SQL.Add(list)

