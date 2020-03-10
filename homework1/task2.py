# -*- encoding: utf-8 -*-
'''
@File : task2.py
@Time : 2020/03/08 21:48:43
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
2 一个字典中，存放了10个学生的学号（key）和分数（value）；请筛选输出，大于80分的同学（按照格式：学号：分数）；
'''

# student_name = ['阿萨德','史蒂夫','算法','大法官','是非观','梵蒂冈','供电局','语句块','御魂','豆腐干']
# student_id = [120180,120181,120182,120183,120184,120185,120186,120187,120188,120189]
# student_score = [20,30,40,50,60,70,80,90,95,100]
# result = dict(zip(student_name,student_id,student_score))   #有问题，不能这么弄，记得查清这种写法怎么弄
# print(result[student_name[0]])

student = []
student1 = {'name':'二狗蛋','id':120180,'score':20}
student2 = {'name':'阿斯蒂芬','id':120181,'score':30}
student3 = {'name':'张铁柱','id':120182,'score':40}
student4 = {'name':'孙二少','id':120183,'score':50}
student5 = {'name':'韩硕','id':120184,'score':60}
student6 = {'name':'滑稽','id':120185,'score':70}
student7 = {'name':'东方贵红','id':120186,'score':80}
student8 = {'name':'橙子','id':120187,'score':90}
student9 = {'name':'苹果','id':120188,'score':96}
student10 = {'name':'草莓','id':120189,'score':100}

student.append(student1)
student.append(student2)
student.append(student3)
student.append(student4)
student.append(student5)
student.append(student6)
student.append(student7)
student.append(student8)
student.append(student9)
student.append(student10)

print("大于80分的同学的学号，分数如下：\n")
for temp in student:
    if temp['score'] >=80:
        print("学号：",temp['id'],"     分数：",temp['score'],"\n")


