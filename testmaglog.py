from PyQt5 import QtCore, QtGui, QtWidgets
import testMagMainWind
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 80, 55, 16))
        self.label.setObjectName("label")

        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(150, 80, 150, 22))
        self.lineEdit_username.setObjectName("lineEdit_username")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 55, 16))
        self.label_2.setObjectName("label_2")

        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(150, 120, 150, 22))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(150, 160, 93, 28))
        self.pushButton_login.setObjectName("pushButton_login")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Window"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton_login.setText(_translate("MainWindow", "Войти"))

class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.check_login)

    # def check_login(self):
    #     username = self.lineEdit_username.text()
    #     password = self.lineEdit_password.text()
    #
    #     if username == "111" and password == "111":
    #         self.open_main_window()
    #     else:
    #         QtWidgets.QMessageBox.critical(self, "Ошибка", "Неверный логин или пароль")

    def check_login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        if self.validate_login(username, password):
            self.open_main_window()
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Неверный логин или пароль")

    def validate_login(self, username, password):
        connection = sqlite3.connect('crm.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM admins WHERE login=? AND pass=?", (username, password))
        result = cursor.fetchone()
        connection.close()
        return result is not None

    def open_main_window(self):
        self.main_window = QtWidgets.QDialog()
        self.ui = testMagMainWind.Ui_Dialog()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = LoginWindow()
    MainWindow.show()
    sys.exit(app.exec_())
