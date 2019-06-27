from tkinter import *
from tkinter import ttk
import socket
import threading
import time

# 定义全局变量
net_status = 0      # 网络连接状态，   0：未连接；1：UDP；2：TCP服务端；3：TCP客户端；
send_permission = 0         # 消息发送许可
net_socket = 0          # 当前套接字或TCP服务端被动套接字
net_socket2 = 0         # TCP服务端与客户端连接的套接字
addr = 0           #地址，（'ip',port）

# 网络连接选择函数
def CONNECT():
    global net_status, net_socket, net_socket2
    if net_status == 0:
        if comboxlist.get() == 'UDP':        # UDP
            UDP()
        elif comboxlist.get() == 'TCP客户端':      # TCP客户端
            TCP_Client()
        elif comboxlist.get() == 'TCP服务端':      # TCP服务端
            TCP_Server()
        else:
            pass
    else:
        net_socket.close()
        net_status = 0
        net_socket = 0
        net_socket2 = 0
        conbt['text'] = '创建连接'
        stateshow_lb['text'] = '未连接'

# UDP函数
def UDP():
    global net_status, net_socket
    ip = str(ipe.get())
    port = int(pte.get())
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((ip, port))
    except:
        stateshow_lb['text'] = '创建失败'
    else:
        stateshow_lb['text'] = '创建成功'
        conbt['text'] = '断开连接'
        udp_recv_thread = threading.Thread(target = UDP_recv, args = (udp_socket,))
        udp_recv_thread.start()
        net_status = 1
        net_socket = udp_socket

# UDP消息接受函数
def UDP_recv(udp_socket):
    global addr
    i = 1
    if net_status == 1:
        try:
            while 1:
                recv_msg = udp_socket.recvfrom(1024)
                recv_ip = recv_msg[1]
                addr = recv_ip
                recv_msg = recv_msg[0].decode("utf-8")
                if i == 1:
                    datarecv_text.insert(END, '消息来自%s:%d'%(recv_ip[0], recv_ip[1]) + '\n')
                    datarecv_text.insert(END, recv_msg + '\n')
                else:
                    datarecv_text.insert(END, recv_ip[0] + recv_msg + '\n')
                    time.sleep(0.1)
                i += 1
        except:
            return


# TCP服务器
def TCP_Server():
    global net_status, net_socket
    ip = str(ipe.get())
    port = int(pte.get())
    try:
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(('%s'%ip, port))
        tcp_server_socket.listen(128)
    except:
        stateshow_lb['text'] = '创建失败'
    else:
        stateshow_lb['text'] = '创建成功'
        conbt['text'] = '断开连接'
        net_socket = tcp_server_socket
        net_status = 2
        tcp_recv_thread = threading.Thread(target = TCP_Recv, args = (tcp_server_socket,))
        tcp_recv_thread.start()
# TCP消息接受线程创建函数
def TCP_Recv(tcp_server_socket):
    global net_socket2, addr
    if net_status == 2:
        try:
            while 1:
                if net_status == 2:
                    net_socket2, addr = tcp_server_socket.accept()
                    tcp_recv_thread = threading.Thread(target = TCP_recv, args = (net_socket2, addr))
                    tcp_recv_thread.setDaemon(True)
                    tcp_recv_thread.start()
        except:
            return
# TCP消息接受函数
def TCP_recv(net_socket2, addr):
    i = 1
    if net_status == 2:
        while 1:
            recv_msg1 = net_socket2.recv(1024)
            if recv_msg1:
                recv_msg = recv_msg1.decode('utf-8')
                if i == 1:
                    datarecv_text.insert(END, '数据来自%s:%d'%(addr[0], addr[1]) + '\n')
                    datarecv_text.insert(END, addr[0] + recv_msg + '\n')
                else:
                    datarecv_text.insert(END, recv_msg + '\n')
            else:
                return
            time.sleep(0.1)

# TCP客户端
def TCP_Client():
    global net_status, net_socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = str(ipe.get())
    port = int(pte.get())
    try:
        tcp_client_socket.connect((ip, port))
    except:
        stateshow_lb['text'] = '创建失败'
    else:
        stateshow_lb['text'] = '创建成功'
        conbt['text'] = '断开连接'
        tcp_recv_thread = threading.Thread(target = TCP_Client_recv, args = (tcp_client_socket,))
        tcp_recv_thread.start()
        net_status = 3
        net_socket = tcp_client_socket
# TCP客户端消息接受
def TCP_Client_recv(tcp_client_socket):
    if net_status == 3:
        try:
            while 1:
                recv_msg = tcp_client_socket.recv(1024)
                recv_msg = recv_msg.decode("utf-8")
                datarecv_text.insert(END, recv_msg + '\n')
                time.sleep(0.1)
        except:
            return

# 发送函数
def SEND():
    if net_status == 1:
        # UDP模式发送
        addr = (str(tagitip_tx.get()), int(tagitpt_tx.get()))
        msg = str(sendarea_tx.get(1.0, 999.999))
        net_socket.sendto(msg.encode('utf-8'), addr)
    elif net_status == 2:
        # TCP客户端发送
        msg = str(sendarea_tx.get(1.0, 999.999))
        net_socket2.send(msg.encode('utf-8'))
    elif net_status == 3:
        # TCP服务端发送
        msg = str(sendarea_tx.get(1.0, 999.999))
        net_socket.send(msg.encode('utf-8'))
    else:
        stateshow_lb['text'] = '未连接'
    time.sleep(0.1)

def CLEAR():             # 清屏
    datarecv_text.delete(1.0, 999.999)

def PUT():               # 快速填入对方地址
    if net_status == 2 or net_status == 1:
        tagitip_tx_e.set(addr[0])
        tagitpt_tx_e.set(addr[1])

def AUTO(event=None):    # 窗口显示内容自动调整
    if comboxlist.get() == 'TCP客户端':
        ipl['text'] = '服务器IP地址        '
        ptl['text'] = '服务器端口          '
    else:
        ipl['text'] = '本地IP地址          '
        ptl['text'] = '本地端口            '

# 窗口
root = Tk()
root.title("网络调试助手")
root.geometry('500x430')
root.resizable(width=False, height=False)

# 网络设置框架
frame_root = LabelFrame(root, text='网络设置', font=('', 10), width=160, height=180, border=2)
frame_1 = Frame(frame_root)     # 协议类型
frame_2 = Frame(frame_root)     # 本地IP地址
frame_3 = Frame(frame_root)     # 本地端口

# 协议类型
xyl = Label(frame_1, text = '协议类型            ', font = ('', 10), width=21, height=1)
xyl.pack(side = TOP)
comvalue = StringVar()
comboxlist = ttk.Combobox(frame_1, textvariable=comvalue, font=('', 9))
comboxlist["values"] = ("UDP", "TCP服务端", "TCP客户端")
comboxlist.current(0)
comboxlist.pack(side=BOTTOM)
comboxlist.bind('<FocusIn>', AUTO)

# 本地IP地址
ipl = Label(frame_2, text='本地IP地址          ', font=('', 10), width=21, height=1)
ipl.pack(side=TOP)
var_ip = StringVar()
ipe = Entry(frame_2, textvariable=var_ip)
ipe.pack(side=BOTTOM)
var_ip.set('127.0.0.1')

# 本地端口
ptl = Label(frame_3, text='本地端口            ', font=('',10), width=21, height=1)
ptl.pack(side=TOP)
var_pt = StringVar()
pte = Entry(frame_3, textvariable=var_pt)
pte.pack(side=BOTTOM)
var_pt.set('8080')

# 连接网络按钮
conbt = Button(frame_root, text='连接网络', command=CONNECT, width=19)
conbt.place(x=4, y=130)

# 画布
canvas = Canvas(root, width=150, height=150, bg='white')
canvas.place(x=10, y=220)
canvas.create_polygon(44,47,25,25,33,56,30,80,35,105,61,120,68,121,92,121,105,116,115,83,117,68,109,57,123,42,124,31,107,37,98,53,109,59,98,53,72,44,44,47,32,56,fill="", outline="black")
canvas.create_polygon(53,69,49,77,56,80,63,74,59,70,fill="", outline="blue")
canvas.create_polygon(92,74,96,82,100,81,102,75,101,70,fill="", outline="blue")
canvas.create_polygon(65,107,73,112,78,111,78,106,75,98,69,94,75,88,81,93,76,99,78,106,82,111,88,111,88,105,88,111,82,111,78,106,78,110,71,113,fill="", outline="black")
canvas.create_polygon(23,93,38,96,54,96,fill="", outline="black")
canvas.create_polygon(27,109,49,101,fill="", outline="black")
canvas.create_polygon(37,117,51,109,fill="", outline="black")
canvas.create_polygon(96,93,113,89,126,83,fill="", outline="black")
canvas.create_polygon(99,97,119,103,fill="", outline="black")
canvas.create_polygon(97,103,117,114,fill="", outline="black")

# 底部状态标签
status_lb = Label(text='状态:', font=('', 10), width=5, height=1)
status_lb.place(x=4, y=400)
stateshow_lb = Label(text='未连接', font=('', 10), width=10, height=1)
stateshow_lb.place(x=40, y=400)

# 网络设置框架放置
frame_1.place(x=0, y=0)
frame_2.place(x=0, y=40)
frame_3.place(x=0, y=80)
frame_root.propagate(0)
frame_root.place(x=10, y=10)

# 数据接受区
datarecv_lb = Label(text='数据接受区            ', font=('', 10), width=21, height=1)
datarecv_lb.place(x=175, y=4)
datarecv_text = Text(height=18, width=44, border=1)
datarecv_text.place(x=176, y=24)

# 数据发送区
tagitip_lb = Label(text='目标IP地址', font=('', 10), width=10, height=1)
tagitip_lb.place(x=173, y=264)
tagitip_tx_e = StringVar()
tagitip_tx = Entry(width=16, textvariable=tagitip_tx_e)
tagitip_tx_e.set('127.0.0.1')
tagitip_tx.place(x=246,y=264)
tagitpt_lb = Label(text='目标端口', font=('', 10), width=8, height=1)
tagitpt_lb.place(x=340, y=264)
tagitpt_tx_e = StringVar()
tagitpt_tx = Entry(width=8, textvariable=tagitpt_tx_e)
tagitpt_tx_e.set(8080)
tagitpt_tx.place(x=400, y=264)
sendarea_tx = Text(height=8, width=32, border=1)
sendarea_tx.place(x=175, y=288)
send_bt = Button(text='发送', height=3, width=8, border=2, command = SEND, font=('', 12))
send_bt.place(x=410, y=310)

put_bt = Button(text='速填', height=1, width=4, border=2, command = PUT, font=('', 9))
put_bt.place(x=465, y=264)

clear_bt = Button(text='清屏', height=1, width=4, border=2, command = CLEAR, font=('', 9))
clear_bt.place(x=120, y=400)

root.mainloop()