# -*- encoding: utf-8 -*-
'''
@File : os.py
@Time : 2020/03/18 08:31:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

#练习6：给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去;

# import os
# import pickle
# data1 = [
#     {'num': '1', 'name': 'amy', 'age': 19},
#     {'num': '2', 'name': 'alice', 'age': 20},
#     {'num': '3', 'name': 'dsfg', 'age': 21},
#     {'num': '4', 'name': 'tsfd', 'age': 22},
#     {'num': '5', 'name': 'lfda', 'age': 23}
# ]

# with open('student.txt', 'w+',encoding='utf-8') as f:
#     pickle.dump(data1, f)
# with open('student.txt', 'r',encoding='utf-8') as f:
#     ldata1 = pickle.load(f)
#     print(ldata1)




# here put the import lib

# import os

# print(os.path.basename('/root/runoob.txt'))
# print(os.path.dirname('root/runboot.txt'))
# print(os.path.split('root/runboot.txt'))
# print(os.path.join('root','test','runoob.txt'))

# f= open("E:\Python\CodeProjects\PythonProjects\opms\homework2\aa.py","r") 
# print(f.read())


# f = open("E:/Python/CodeProjects/PythonProjects/opms/homework2/1topic.txt","r")
# print(f.read())


# import sys ,os

# print(os.getcwd()) 
# print("aytjuyiuoi")




# path1 = r"E:\桌面\文件夹1\test1.txt"
# path2 = r"E:\桌面\文件夹2\test2.txt"
# copy(path1,path2)



# import os
# import time
 
# file='E:/Python/CodeProjects/PythonProjects/opms/homework2/1topic.txt' # 文件路径
 
# print( os.path.getatime(file) )   # 输出最近访问时间
# print( os.path.getctime(file) )   # 输出文件创建时间
# print( os.path.getmtime(file) )   # 输出最近修改时间
# print( time.gmtime(os.path.getmtime(file)) )  # 以struct_time形式输出最近修改时间
# print( os.path.getsize(file) )   # 输出文件大小（字节为单位）
# print( os.path.abspath(file) )   # 输出绝对路径
# print( os.path.normpath(file) )  # 规范path字符串形式



'''
练习3:   一个文件内容的如下,请读取文件的内容, 并输出;
            姓名      学号      分数
            张三      101         78
            李四      102         87
            王五       103        83
'''
# with open('student.txt','r',encoding='utf-8')as f:
#     f.readline()



'''
练习4
:   一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
            姓名      学号      分数
            张三      101         78
            李四      102         87
            王五       103        83
'''
# f=open(r'11.txt', 'r', encoding='utf-8')  
# f2=open(r'studnet.txt', 'w', encoding='utf-8')
# l=[]
# sort=[]
# for line in f:
#         list = line.split() 
#         l.append(list[2])
#         sort=sorted(l)

# f2.write(sort[0]+"\n")
# f2.write(sort[1]+"\n")
# f2.write(sort[2]+"\n")
# f.close()
# f2.close()




'''
练习5：一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出;
            姓名      学号      分数
            张三      101         78
            李四      102         87
            王五       103        83
'''
with open(r'11.txt', 'r', encoding='utf-8') as f:
    l=[]
    sort=[]
    for line in f:  # 遍历每一行
            list = line.split()  # 将每一行的数字分开放在列表中
            l.append(list[2])
            sort=sorted(l)
    print(sort[0])
    print(sort[1])
    print(sort[2])
    

