# -*- encoding: utf-8 -*-
'''
@File : task1.py
@Time : 2020/03/08 20:54:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
1 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数
'''

list1 = []
list2 = []
list3 = []
list4 = []
for i in range(0,51):
    if i%2 != 0:
        list1.append(i)
    if i%2 == 0:
        list2.append(i)
    if i%2 == 0 and i%3 == 0:
        list4.append(i)

for x in range(2,51):
    for y in range(2,i):
        if x%y == 0:
            break 
        else:
            list3.append(x)
            break

print("0-50之间的奇数为：",list1,"\n")
print("0-50之间的偶数为：",list2,"\n")
print("0-50之间的质数为：",list3,"\n")
print("0-50之间的能同时被2和3整除的数为：",list4,"\n")
