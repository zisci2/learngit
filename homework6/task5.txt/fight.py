#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File : task5.py
@Time : 2020/04/24 00:15:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
'''
五  请写一个小游戏，人狗大站;  规则:
    1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
        人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
    2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
        人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
    3   对战规则: 
     A  随机决定,谁先开始攻击; 
     B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
     C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
     
提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件； 在写一个fight模块（也用类来组织；
在这个模块中，导入人和狗模块中编写好的方法
'''

import People
import Dog
import random

if __name__ == "__main__":
    print("游戏开始~~")
    print("\n")
    p0 = People.people(0)
    p1 = People.people(1)
    p = [p0,p1]
    d0 = Dog.dog(0)
    d1 = Dog.dog(1)
    d2 = Dog.dog(2)
    d = [d0,d1,d2]
    count = random.randint(0,1)  ##0狗咬人，1人打狗
    while True:

        if count == 0 and len(p) >0 and len(d) >0:  ##狗攻击人
            num1 = random.randint(0,len(d)-1)  ##狗子
            num2 = random.randint(0,len(p)-1)   ##人
            print("小狗{}号咬了{}号人一口".format(d[num1].name,p[num2].name))
            p[num2].be_attacked(d[num1].attack)
            print("{}号人，血量还剩{}，攻击力还剩{}".format(p[num2].name,p[num2].blood,p[num2].attack))
            if p[num2].blood <= 0:
                print("{}号人失血过度，离我们远去了~~~".format(p[num2].name))
                p.remove(p[num2])
            count = 1
            print("\n")
        if count == 1 and len(p) >0 and len(d) >0:  ##人攻击狗
            num1 = random.randint(0,len(d)-1)  ##狗子
            num2 = random.randint(0,len(p)-1)  ##人
            print("{}号大人打了{}号小狗一棍".format(p[num2].name,d[num1].name))
            d[num1].be_attacked(p[num2].attack)  ##扣血，扣攻击
            print("{}号小狗，血量还剩{}，攻击力还剩{}".format(d[num1].name,d[num1].blood,d[num1].attack))
            if d[num1].blood <= 0:
                print("{}号狗子失血过度，离我们远去了~~~".format(d[num1].name))
                d.remove(d[num1])
            count = 0
            print("\n")
                
        if (len(p) == 0):  
            print("狗狗胜利，人全被咬死了~~~")
            break
        if (len(d) == 0):
            print("人胜利，小狗全被打死了~~~")
            break
