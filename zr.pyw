from tkinter import *
from tkinter import messagebox
import socket
import time
import threading
# root.wm_attributes('-toolwindow',1)

# w = root.winfo_screenwidth()
# h = root.winfo_screenheight()
# root.geometry('%dx%d'%(w,h))
# root.attributes('-topmost',1)

def Connect():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcp_client_socket.connect(('192.168.46.49', 1503))
    except:
        lb['text']='连接失败'
        show.insert(END,'未连接到服务器，无法享受到该服务')
        button2['text']='遗憾离开'
        return
    else:
        lb['text']='连接成功'
    recv_th = threading.Thread(target=recvmsg,args=(tcp_client_socket,),daemon=True)
    recv_th.start()
def recvmsg(tcp_client_socket):
    while 1:
        msg_by = tcp_client_socket.recv(1024)
        msg = msg_by.decode('utf-8')
        show.insert(END,msg)
def Donation():
    select = messagebox.askokcancel(title='Hi', message='支付100Y？')
    if select:
        button1['text']='感谢！'
        time.sleep(1)
        exit()
    else:
        pass
def EXIT():
    # messagebox.showinfo(title='Hi', message='hahahaha')
    select = messagebox.askokcancel(title='Hi', message='你真的要离开吗？')
    if select:
        button2.destroy()
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        root.geometry('%dx%d'%(w,h))
        show.pack(fill='x')
        button1['font']=('', 80)
        button1.place(anchor='n',x=w/2,y=h/2)

def MOVE(event=None):
    global i
    if i < 10:
        if i%3==0:
            button2.place(x=170, y=250)
            button2['text'] = '我在这儿'
        elif i%3==1:
            button2['text'] = '来抓我呀'
            button2.place(x=170, y=350)
        elif i%3==2:
            button2['text'] = '我又到这儿了'
            button2.place(x=170, y=300)
    else:
        button2['text'] = '跑不动了，你点吧。。'
        button2.place(x=170, y=300)
    i += 1
def callback():
    # messagebox.showwarning('警告', '回答问题')
    select = messagebox.askokcancel(title='Hi', message='你真的要离开吗？')
    if select:
        while 1:
            messagebox.showwarning('警告', '你的良心不会痛吗？')
            time.sleep(1)
    else:
        pass


root = Tk()
root.title("一个奇怪的小软件")
root.geometry('300x400')
root.resizable(width=False, height=False)
root.attributes('-topmost',1)

i = 0

# f = Frame(root,background='blue',borderwidth=1)
f = Frame(root)
f.pack(side='top',fill='x')

lb = Label(f,text='正在连接服务器', font=('', 10),  height=1)
lb.pack(side='top',fill='x')


sb = Scrollbar(f)
sb.pack(side='right',fill='y')

show = Text(f,yscrollcommand=sb.set, height=15, width=38)
show.pack(side='top')

sb.config(command=show.yview)

button1 = Button(root, text='捐助作者', command=Donation)
button1.place(x=70, y=300)
button2 = Button(root, text='无情离开', command=EXIT)
button2.place(x=170, y=300)
button2.bind('<Enter>',MOVE)



Connect()
root.wm_protocol('')
root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()