# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signupform.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SigninWindow(object):
    def setupUi(self, SigninWindow):
        SigninWindow.setObjectName("SigninWindow")
        SigninWindow.resize(439, 745)
        self.centralwidget = QtWidgets.QWidget(SigninWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_Signin = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Signin.setGeometry(QtCore.QRect(40, 20, 361, 591))
        self.groupBox_Signin.setObjectName("groupBox_Signin")
        self.label_email = QtWidgets.QLabel(self.groupBox_Signin)
        self.label_email.setGeometry(QtCore.QRect(0, 40, 120, 25))
        self.label_email.setFrameShape(QtWidgets.QFrame.Box)
        self.label_email.setLineWidth(2)
        self.label_email.setObjectName("label_email")
        self.edittext_email = QtWidgets.QLineEdit(self.groupBox_Signin)
        self.edittext_email.setGeometry(QtCore.QRect(150, 40, 150, 25))
        self.edittext_email.setObjectName("edittext_email")
        self.label_password = QtWidgets.QLabel(self.groupBox_Signin)
        self.label_password.setGeometry(QtCore.QRect(0, 120, 120, 25))
        self.label_password.setFrameShape(QtWidgets.QFrame.Box)
        self.label_password.setLineWidth(2)
        self.label_password.setObjectName("label_password")
        self.edittext_password = QtWidgets.QLineEdit(self.groupBox_Signin)
        self.edittext_password.setGeometry(QtCore.QRect(150, 120, 150, 25))
        self.edittext_password.setObjectName("edittext_password")
        self.btn_signin = QtWidgets.QPushButton(self.groupBox_Signin)
        self.btn_signin.setGeometry(QtCore.QRect(120, 170, 111, 32))
        self.btn_signin.setObjectName("btn_signin")
        SigninWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SigninWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 22))
        self.menubar.setObjectName("menubar")
        SigninWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SigninWindow)
        self.statusbar.setObjectName("statusbar")
        SigninWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SigninWindow)
        QtCore.QMetaObject.connectSlotsByName(SigninWindow)

    def retranslateUi(self, SigninWindow):
        _translate = QtCore.QCoreApplication.translate
        SigninWindow.setWindowTitle(_translate("SigninWindow", "MainWindow"))
        self.groupBox_Signin.setTitle(_translate("SigninWindow", "Sign In"))
        self.label_email.setText(_translate("SigninWindow", "Email:"))
        self.label_password.setText(_translate("SigninWindow", "Password"))
        self.btn_signin.setText(_translate("SigninWindow", "Sign In"))
