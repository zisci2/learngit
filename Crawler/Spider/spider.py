#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author：zsw time:2020-6-20
'''
5 爬虫程序：
     给定10万个企业的网址（放在数据库表中），请编写一个网络爬虫，
     爬取该企业的产品及服务信息（即获取该企业能提供的产品和服务）；
     并将爬取到的数据，保存到数据库中；请自行设计数据库表结构
'''

import re,requests
from bs4 import BeautifulSoup
import SQL
from multiprocessing import Pool

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

#解析数据
def getData(url):
    h_text = getHtmlText(url)
    if h_text == "404":
        return "404"
    else:
        #十万个网址里，有些企业产品信息放在官网首页，但更多的是放在链接
        #所以选择大多数，先找到链接
        soup = BeautifulSoup(h_text,'html.parser')
        label = soup.findAll('a',text=re.compile(r"产品|服务"))
        for i in label:
            href = i.get('href')
            M_url = href
            if href != None:
                if 'http' in href:
                    M_url = href
                else:
                    s = url+'/'+href
                    M_url = s
            #提取信息
            list = []
            h1_text = getHtmlText(M_url)
            soup_test = BeautifulSoup(h1_text,'html.parser')

            text = soup_test.find_all(text=True)
            final = ''
            blacklist = [
                '[document]','noscript','header','html','meta','head','input','script',
                '</a></span>','<a><span>',
            ]  #去掉不想要的元素

            for t in text:
                if t.parent.name not in blacklist:
                    final += '{}'.format(t)
            return final






#保存信息
def save(id):
    list_url = SQL.get_url(id)
    num = len(list_url)
    a = 0
    while a < num-1 :  #有些企业的网址不止一个，但有些不能正确响应
        if getHtmlText(list_url[a]) != '404':
            break
        else:
            a += 1
        if a == num-1:
            break
    text = getData(list_url[a])
    if text != None:   #有这么一种情况，网页响应了，但里面没有匹配到内容，所以
        SQL.Add(text,id)
    else:
        SQL.Add("暂未找到", id)

#
# save(1)
#
if __name__ =='__main__':
    po = Pool(8)
    for i in range(1,20):
        po.apply_async(save,(i,))

    print("-----star----")
    po.close()
    po.join()
    print("-----end-----")