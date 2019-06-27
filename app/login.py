# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pwdbox(object):
    def setupUi(self, pwdbox):
        pwdbox.setObjectName("pwdbox")
        pwdbox.resize(320, 420)
        pwdbox.setMinimumSize(QtCore.QSize(320, 420))
        pwdbox.setMaximumSize(QtCore.QSize(320, 420))
        self.centralwidget = QtWidgets.QWidget(pwdbox)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 120, 179, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        pwdbox.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pwdbox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 23))
        self.menubar.setObjectName("menubar")
        pwdbox.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pwdbox)
        self.statusbar.setObjectName("statusbar")
        pwdbox.setStatusBar(self.statusbar)

        self.retranslateUi(pwdbox)
        QtCore.QMetaObject.connectSlotsByName(pwdbox)

    def retranslateUi(self, pwdbox):
        _translate = QtCore.QCoreApplication.translate
        pwdbox.setWindowTitle(_translate("pwdbox", "MainWindow"))
        self.pushButton.setText(_translate("pwdbox", "登录"))
        self.pushButton_2.setText(_translate("pwdbox", "注册"))
        self.label.setText(_translate("pwdbox", "用户名"))
        self.label_2.setText(_translate("pwdbox", "密  码"))

