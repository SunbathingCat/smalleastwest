import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import *
import time
import sqlite3
import os
from mymods.random_str import randstr
import hashlib
from mymods.JiaMi.AES import *
from Cryptodome.Cipher import AES
from Cryptodome import Random

class MyWindow(QMainWindow, Ui_pwdbox):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Login)
        self.pushButton_2.clicked.connect(self.Register)

    def Login(self):
        name = myWin.lineEdit.text()
        password = myWin.lineEdit_2.text()
        with SQLITE('user') as c:
            user = c.execute("SELECT name FROM password WHERE NAME='{}'".format(name)).fetchall()
            if len(user)==0:
                print('no user')
                return False
            user = user[0][0]
            pwd = c.execute("SELECT password FROM password WHERE NAME='{}'".format(name)).fetchall()
            pwd = pwd[0][0]
            if pwd == password:
                print('su')
            else:
                print('fail')



    def Register(self):
        name = myWin.lineEdit.text()
        password = myWin.lineEdit_2.text()
        with SQLITE('user') as c:
            c.execute("INSERT INTO password (name,password,islogin) \
                  VALUES ('{}','{}',1 )".format(name,password))


class newThread(QtCore.QThread):
    def run(self):
        while True:
            a = myWin.lineEdit.text()
            time.sleep(0.1)


# with上下文处理sqlite数据库
class SQLITE():
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.conn  = sqlite3.connect('{}.db'.format(self.db))
        self.c = self.conn.cursor()
        return self.c

    def __exit__(self, *args):
        self.conn.commit()
        self.conn.close()
# 判断是否第一次运行来决定是否对数据库初始化
def IsFirst():
    curentDir = os.getcwd()
    doculist = os.listdir(curentDir)
    print(curentDir)
    print(doculist)
    for docu in doculist:
        if docu.find('.db')!=-1:
            break
    else:
        SqlliteInitFir('user')
    for docu in doculist:
        if docu.find('.xms')!=-1:
            break
    else:
        SecretDocumentInit()

def SecretDocumentInit():
    with open('重要文件请勿删除.xms','w') as f:
        f.write(randstr(1024,'szf'))

def SqlliteInitFir(db):
    try:
        with SQLITE(db) as c:
            c.execute('''CREATE TABLE password (
    id       INTEGER PRIMARY KEY AUTOINCREMENT
                     UNIQUE
                     NOT NULL,
    name     TEXT    NOT NULL,
    cate     TEXT,
    password TEXT    NOT NULL,
    other    TEXT,
    islogin  BOOLEAN
);''')
    except:
        print('en')

def MD5Calcu(docu):
    file = open(docu,'rb')
    thismd5 = hashlib.md5(file.read()).hexdigest()
    file.close()
    return thismd5

def GetKey():
    curentDir = os.getcwd()
    doculist = os.listdir(curentDir)
    for docu in doculist:
        if docu.find('.xms')!=-1:
            return MD5Calcu(docu)

def ThansPWD(str):
    str1 = GetKey()
    str2 = str + str1
    p_mima = hashlib.md5(str2.encode('utf-8')).hexdigest()
    print(p_mima)
    mima1 = ''
    for i,s in enumerate(p_mima):
        if i % 2 == 0:
            mima1 += s
    print(mima1)
    mima2 = hashlib.md5(mima1.encode('utf-8')).hexdigest()
    return mima2

def jiamiPWD(str):
    iv = Random.new().read(AES.block_size)
    with SQLITE('user') as c:
        password = c.execute("SELECT password FROM password WHERE islogin=1").fetchall()
        if len(password) == 0:
            print('no user')
            return False
        password = password[0][0]
    salt = password+GetKey()
    key = hashlib.md5(salt.encode('utf-8')).hexdigest()
    key = key[::2]
    return AES_en(key,iv,str)

def jiemiPWD(str):
    with SQLITE('user') as c:
        password = c.execute("SELECT password FROM password WHERE islogin=1").fetchall()
        if len(password) == 0:
            print('no user')
            return False
        password = password[0][0]
    salt = password+GetKey()
    key = hashlib.md5(salt.encode('utf-8')).hexdigest()
    key = key[::2]
    return AES_de(key,str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    IsFirst()
    print(GetKey())
    print(ThansPWD('123456'))
    print(jiamiPWD('qwert'))
    print(jiemiPWD(jiamiPWD('qwert')))
    # myThread = newThread()
    # myThread.start()
    sys.exit(app.exec_())