# -*- encoding: utf-8 -*-
'''
@File : task1.py
@Time : 2020/03/24 15:11:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，
将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
'''

def _input():
    list = []
    while True:
        s = input()
        if not s:     #最初想的是如何表示空格、空行，不知道输入为空怎么办
            return list
        list.append(s)

print("请输入内容，空行为结束：")
try:
    f = open("E:\桌面\input.txt","w") 
    for line in _input():
        f.write(line)
        f.write("\n")
except EOFError:
    print("写入内容出现问题，请检查")
finally:
    f.close()

