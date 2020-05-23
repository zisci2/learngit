import socket
import datetime

def get_ip():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip

def  get_time():
    now = datatime.datatime.now()
    sed_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return sed_time

