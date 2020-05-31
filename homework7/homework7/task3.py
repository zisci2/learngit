#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task3.py
@Time : 2020/04/25 17:55:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
3  给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
     这些音频文件 在网页的html文件内容都是以mp3结尾的，如下图所示：

   要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；
  Windows上的wget可以点击这里 下载。 这个程序不用安装，直接在命令行里使用即可；
注意：
获取的音频网址前面需要加上 前缀 http://www.listeningexpress.com/studioclassroom/ad/ 才是完整的下载地址
MP3文件中有空格字符，组成下载网址时，需要进行url编码，否则空格会被当成命令行分隔符。参考代码如下所示
>>> from urllib.parse import quote
>>> quote('2019-04-13 NEWSworthy Clips.mp3')
'2019-04-13%20NEWSworthy%20Clips.mp3'
'''

from urllib.parse import quote
import requests
import re
from bs4 import BeautifulSoup
import urllib.request

def get_music():
    soup = requests.get("http://www.listeningexpress.com/studioclassroom/ad/")
    soup.encoding = soup.apparent_encoding
    #print(soup.text)
    b_soup = BeautifulSoup(soup.text,'html.parser')
    for i in b_soup.findAll('a'):
        href = i.get("href")
        ad = re.search(r"sc-ad.+\.mp3",href)
        #print(href)
        if ad:
            #print(ad.group())
            ad1 = 'http://www.listeningexpress.com/studioclassroom/ad/'+quote(ad.group())
            # res = requests.get(ad1)
            # music = res.content
            # with open('music\\'+str(ad.grou()),'ab') as f:
            #     f.write(music)   #所有音频连在一起了
            print("下载中...")
            urllib.request.urlretrieve(ad1,'E:\Python\homework7\music\\'+str(ad.group()))
    print("下载完毕")

if __name__ == '__main__':
    get_music()