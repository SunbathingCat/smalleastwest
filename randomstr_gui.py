import random
from tkinter import *

def num():
    '''生成随机数字'''
    i = str(random.randint(0, 9))
    return i
def alp():
    '''生成随机字母'''
    if random.randint(0, 1):  # 随机大小写
        s = chr(random.randint(65, 90))
    else:
        s = chr(random.randint(97, 122))
    return s
def sym():
    '''生成随机符号'''
    sy = ['@', '#', '$', '%', '&', '*']
    s = sy[random.randint(0, 5)]
    return s
def ranfun(typ):
    '''根据密码组成选择随机函数'''
    optnas = [num(), alp(), sym()]
    optna = [num(), alp()]
    optas = [alp(), sym()]
    optns = [num(), sym()]
    if typ == 2:
        return optnas[0]
    elif typ == 1:
        return optnas[1]
    elif typ == 4:
        return optnas[2]
    elif typ == 3:
        return optna[random.randint(0, 1)]
    elif typ == 5:
        return optas[random.randint(0, 1)]
    elif typ == 6:
        return optns[random.randint(0, 1)]
    elif typ == 7:
        return optnas[random.randint(0, 2)]
    else:
        t.insert(END,'输入有误')
def creat():
    long = int(e.get())
    password = ''
    for i in range(0, long):
        password = password + ranfun(typ)
    t.insert(END,password + '\n')
# def cs():
#     t.insert(END, 'hello tom\n')
def checkfun():
    global typ
    typ = 0
    typ = CheckVar1.get() + CheckVar2.get() + CheckVar3.get()

typ = 0
root = Tk()
root.title("密码生成器")
root.geometry('300x300')
root.resizable(width=False, height=False)

head = Label(root, text="密码生成器", font=("Arial", 12), height=2)
head.pack(side=TOP)

pwd_type = Label(root, text='选择密码组成类型：')
pwd_type.place(x=0, y=40)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(text="str", variable=CheckVar1,
                 onvalue=1, offvalue=0, height=2,
                 width=2, command = checkfun)
C2 = Checkbutton(text="num", variable=CheckVar2,
                 onvalue=2, offvalue=0, height=2,
                 width=2, command = checkfun)
C3 = Checkbutton(text="smb", variable=CheckVar3,
                 onvalue=4, offvalue=0, height=2,
                 width=2, command = checkfun)
C1.place(x=108, y=32)
C2.place(x=158, y=32)
C3.place(x=208, y=32)

pwd_num = Label(root, text='输入密码位数：')
pwd_num.place(x=0, y=80)
var = StringVar()
e = Entry(root, textvariable=var)
var.set("5")
e.place(x=90, y=80, anchor=NW)

Button(root, text='点击生成', command=creat).place(x=120, y=110)

t = Text(root, height=8, width=40)
t.place(x=8, y=150)
root.mainloop()








