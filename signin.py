from validateemail import validate_email
from Users import User
from datetime import datetime, date
from database import Database
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Signinform import Ui_SigninWindow

db = Database('store.db')
users = db.fetch()

class SignIn(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignIn, self).__init__()
        self.ui = Ui_SigninWindow()
        self.ui.setupUi(self)
        self.ui.btn_signin.clicked.connect(self.Login)
    
    def Login(self):
        email = self.ui.edittext_email.text()
        password = self.ui.edittext_password.text()
        for user in users:
            if email == user[2] and password == user[3]:
                QtWidgets.QMessageBox.warning(self, "Başaralı", f"Welcome {user[1]}", QtWidgets.QMessageBox.Ok)
                return
        QtWidgets.QMessageBox.warning(self, "başarısız", "Please a valid email", QtWidgets.QMessageBox.Ok)