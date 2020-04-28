#定义一个字典,存放某个同学的信息(学号,姓名,班级,年龄);
# 再定义另外一个字典,存放5个同学的学号,姓名信息;
#    通过键来访问相应的数据; 或者整体输出

dict1 = {'id':120181,'name':"小黑",'class':'class2','age':19}
dict2 = {'id1':12,'name':'qw',
        'id2':34,'name':'ww',
        'id3':45,'name':'ew',
        'id4':56,'name':'rw',
        'id5':67,'name':'tw'}

print(dict1)
print(dict2['id2'])