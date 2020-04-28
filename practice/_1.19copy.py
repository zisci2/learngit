'''
拷贝文件
'''
def  copy(path1,path2):
    list = []
    f1 = open(path1,"r",encoding="utf8")
    a1 = f1.read()
    f2 = open(path2,"w",encoding="utf8")
    f2.write(a1)
    print("复制成功！")
