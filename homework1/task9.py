# -*- encoding: utf-8 -*-
'''
@File : task9.py
@Time : 2020/03/09 01:26:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
9 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
'''
print("我们来玩个游戏呀~~~")
print("猜一下我心中想的数字(提示一下，数字在0到100之间，你有五次猜想机会)")

i = 5
while i >0:
    num = int(input("输入你认为的数字:"))
    if num == 10:
        print("什么？！居然猜对了，真是住在我心中的的人啊~")
    else:
        i=i-1
        print("嘿嘿，没想到吧，猜错了")
        if i !=0:
            print("算了，我这么大气，再给你",i,"次机会吧")

    if i == 0:
        print('''太伤心你居然没有猜对，亏我这么相信你.
        滚，你没机会了''')