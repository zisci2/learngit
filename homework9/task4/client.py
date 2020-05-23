import socket
import threading
import os
import get

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ('127.0.0.1',10000)
s.connect(addr)

def recv_msg():
    print("连接成功！现在可以接受消息！\n")
    while True:
        try:
            response = s.recv(1024)
            print(response.decode("gbk"))
        except ConnectionAbortedError:
            print("服务器关闭，聊天结束！")
            s.close()
            break
    os._exit(0)

def send_msg():
    print("连接成功！可以开始聊天！")
    print("输入消息按回车键发送")
    print("输入esc来退出聊天")
    while True:
        msg = input()
        if msg == 'esc':
            print("你退出了聊天")
            s.close()
            break
        s.send(msg.encode("gbk"))
    os._exit(0)

threads= [threading.Thread(target=recv_msg),threading.Thread(target=send_msg)]
for i in threads:
    i.start()