#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task2.py
@Time : 2020/04/25 17:55:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
    提示：要用到requests库，BeautifulSoup库
'''

import requests,re
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        r = requests.get(url,timeout=10)
        r.raise_for_status()  #200正常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("网页访问产生异常")
        return 404

def getUrl(url):
    h_text = getHtmlText(url)
    if h_text == 404:
        pass
    else:
        soup = BeautifulSoup(h_text,'html.parser')
        # label = soup.find_all('a')
        # for i in label:
        #     ss = i.get("href")
        label = soup.findAll('a',text=re.compile(r"企业介绍|关于我们|企业发展|发展历史|企业概况"),limit=1) #需要限制，否则就会打印多次
        for la in label:
            href = la.get("href")
            if href != None:
                if 'http' in href:
                    print(href)
                else:
                    print(url+'/'+href)
            else:
                print("没有介绍")


if __name__ == '__main__':
    # getUrl("http://www.chrtc.cn")
    num = 0
    with open("message.txt",'r',encoding='utf-8') as f:
        for url in f.readlines():
            url = url.strip('\n')  #之前一直错在与因为表述为：url.strip('\n') ，
            # url = url.rstrip('\n')
            url = url.split(';')
            #print(url[0])
            getUrl(url[0])
            num +=1
            if num >=100:
                break

