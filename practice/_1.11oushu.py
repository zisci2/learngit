#创建一个有10个数字的列表,先输出此列表,然后再输出其中为偶数元素;
s1=list(range(10))
print(s1)
s2 = []
for a in s1:
    if(a%2==0):
        s2.append(a)
print(s2)