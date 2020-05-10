from validateemail import validate_email
from Users import User
from datetime import datetime, date
from database import Database
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from signupform import Ui_MainWindow
from signin import SignIn

db = Database('store.db')
users = db.fetch()
class SignUp(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignUp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_signin.clicked.connect(self.openSigninPage)
        self.ui.btn_signup.clicked.connect(self.createUser)

    def createUser(self):
        nameSurname = self.ui.edittext_namesurname.text()
        email = self.ui.edittext_email.text()
        password = self.ui.edittext_password.text()
        confirm_password = self.ui.edittext_confirm_password.text()
        birthdate = self.ui.birthdate.text()
        if nameSurname == "" or email == "" or password == "" or confirm_password == "" or birthdate == "":
            QtWidgets.QMessageBox.warning(self, "EMPTY FIELDS !", "All fields are required", QtWidgets.QMessageBox.Ok)
        elif password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "PASSWORD ERROR", "Passwords do not match", QtWidgets.QMessageBox.Ok)
        elif not validate_email(email):
            QtWidgets.QMessageBox.warning(self, "EMAIL ERROR", "Please enter a valid email", QtWidgets.QMessageBox.Ok)
        else:
            for user in users:
                if email == user[2]:
                    QtWidgets.QMessageBox.warning(self, "Sorry!", "This email already taken!!", QtWidgets.QMessageBox.Ok)
                    return
            
            db.insert(nameSurname, email, password, confirm_password, birthdate)
            QtWidgets.QMessageBox.warning(self, "Thanks!", "Your informations saved succesfully!", QtWidgets.QMessageBox.Ok)

    def openSigninPage(self):
        self.close()
        self.newWindow = SignIn() 
        self.newWindow.show()

        
        


def app():
    signup_app = QtWidgets.QApplication(sys.argv)
    win = SignUp()
    win.show()
    sys.exit(signup_app.exec_())

app()