# -*- encoding: utf-8 -*-
'''
@File : tsak4.py
@Time : 2020/03/15 10:44:38
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
4  写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
'''

def total():
    char_num = 0
    num_num = 0
    space_num = 0
    other_num = 0
    str = input("请输入想要统计的字符串：")
    for char in str:
        if char.isalpha():
            char_num += 1
        elif char.isdigit():
            num_num += 1
        elif char.isspace():
            space_num += 1
        else:
            other_num += 1

    print("该字符串的总长度为：",len(str))
    print("该字符串中字母的个数为：",char_num)
    print("该字符串中数字的个数为：",num_num)
    print("该字符串中空格的个数为：",space_num)
    print("该字符串中其他字符的个数为：",other_num)

total()