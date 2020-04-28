#将这4中方式实现的代码分别在vscode上练习一下;

#第一种方法：字符串拼接 + （不建议使用，太耗内存）

# username = input('username:')
# password = input('password:')
# print(username,password)



#第二种用法：%s（代表字符串） %d（代表数字，可以用作验证、检测数据类型）%f（浮点类型

# name = input("name:")
# age = input("age:")
# skill = input("skill:")
# salary = input("salary:")
# info = ''' --- info of ''' + name + ''' name: ''' + name + ''' age: ''' + age + ''' skill: ''' + skill + ''' salary: ''' + salary + ''' '''
# print(info)



#第三种用法：使用{参数名}，在有的特殊情况下，一定要使用这样的格式，比如监控

# name = input("username：")
# age = input("age：")
# skill = input("skill：")
# salary = input("salary：")
#info = ''' --- info of {_name} Name：{_name} Age：{_age} Skill：{_skill} Salary：{_salary} '''.format(_name=name, _age=age, _skill=skill, _salary=salary) #此处是赋值 print(info)



#第四种用法：{索引}

name = input("name：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")
info = ''' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '''.format(name, age, skill, salary)

print(info)