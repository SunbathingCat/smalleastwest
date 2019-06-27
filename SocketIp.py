'''
利用udp每10秒广播一次自己的IP
utf-8格式的结果广播至1504端口
gbk格式的结果广播至1503端口
自己2504端口接受到close后程序结束
'''
import socket
import time
import threading
import subprocess
import platform
import os

#接受线程，2504端口收到‘close’后关闭程序
def recvmsg(ip_socket,ip_socket2):
    while 1:
        recv_data = ip_socket2.recvfrom(1024)
        if recv_data[0].decode('utf-8') == 'close' or recv_data[0].decode('gbk') == 'close':
            ip_socket.sendto('end\n'.encode('gbk'), ('255.255.255.255', 1503))
            ip_socket.sendto('end\n'.encode('utf-8'), ('255.255.255.255', 1504))
            ip_socket.close()
            ip_socket2.close()
            os._exit(0)     #线程中结束程序，0：无报错退出


if platform.system() == 'Windows':
    ipconfig_process = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
    output = ipconfig_process.stdout.read().decode("gbk")
else:
    ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
    output = ipconfig_process.stdout.read().decode("utf-8")

#广播用socket
ip_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_socket.bind(('', 2503))
ip_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

#接受用socket
ip_socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_socket2.bind(('', 2504))

recv_threading = threading.Thread(target=recvmsg, args=(ip_socket,ip_socket2),daemon=True)
recv_threading.start()

i = 1
while True:
    senddata = output + '\n第' + str(i) + '次发送,发close至2504端口关闭'

    # gbk 编码发至 1503 端口，utf-8编码发至 1504 端口
    ip_socket.sendto(senddata.encode('gbk'), ('255.255.255.255', 1503))
    ip_socket.sendto(senddata.encode('utf-8'), ('255.255.255.255', 1504))
    i += 1
    time.sleep(10)