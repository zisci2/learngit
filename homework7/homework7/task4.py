#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task4.py
@Time : 2020/04/25 17:56:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
4 爬取这个网址上https://www.programcreek.com/python/?ClassName=request&submit=Search，所有的Python练习题题目和答案；保存到txt文件中（只保留文字）；
    文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：

  参考文档：https://blog.csdn.net/weixin_43687366/article/details/88877996
   大家看完这篇文档后，再开始动手做这道题；

'''
from bs4 import BeautifulSoup
import requests

url = 'https://www.programcreek.com/python/index/1091/urllib.request'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 \
Safari/537.36 Edge/18.18362'}
html = requests.get(url,headers=headers).content.decode('utf-8')
# print(html)
soup = BeautifulSoup(html,'html.parser')
re_a = soup.find(id='api-list').find_all('a')

list = []
for i in re_a:
    list.append(i.attrs['href'])

# for i in list:
#     print(i)

data = []
for i in list:
    dict = {}
    test = requests.get(i,headers=headers).content.decode("utf-8")
    soup_test = BeautifulSoup(test,'html.parser')
    #print(test)
    dict['title'] = soup_test.find(id='main').h1.text
    try:
        dict['code'] = soup_test.find(class_='prettyprint').text
    except Exception as e:
        dict['code'] = soup_test.find('pre').text

    with open('practice python.txt','a+',encoding='utf-8')as f:
        f.write(dict['title']+'\n')
        print(dict['title']+'\n')
        f.write(dict['code']+'\n')
        print(dict['code']+'\n')
        f.write('\n')
        f.write('#'*100+'\n')
        f.write('\n')



