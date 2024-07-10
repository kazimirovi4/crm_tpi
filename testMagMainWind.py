from PyQt5 import QtCore, QtGui, QtWidgets
import testmagbuywind
import sqlite3
import addwind

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1123, 867)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 50, 181, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 50, 181, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 50, 181, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(840, 50, 181, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 180, 961, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(70, 280, 961, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        self.tableWidget.setHorizontalHeaderLabels([
            "Вид транзакции", "Клиент", "Артикул товара", "Ответственное лицо", "Дата", "Время", "Статус транзакции"])

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.resizeColumnToContents(3)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_4.clicked.connect(self.open_testmagbuywind)
        self.lineEdit.textChanged.connect(self.filter_table)
        self.pushButton.clicked.connect(self.open_addwind)

        self.load_data()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Добавить"))
        self.pushButton_2.setText(_translate("Dialog", "***"))
        self.pushButton_3.setText(_translate("Dialog", "***"))
        self.pushButton_4.setText(_translate("Dialog", "Новая транзакция"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Поиск транзакций"))

    def open_testmagbuywind(self):
        self.buy_window = QtWidgets.QDialog()
        self.ui_buy = testmagbuywind.Ui_Dialog()
        self.ui_buy.setupUi(self.buy_window)
        self.buy_window.show()

    def open_addwind(self):
        self.add_window = QtWidgets.QDialog()
        self.ui_add = addwind.Ui_Dialog()
        self.ui_add.setupUi(self.add_window)
        self.add_window.show()

    def load_data(self):
        conn = sqlite3.connect('crm.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Заказы')
        rows = c.fetchall()

        self.tableWidget.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

        conn.close()

    def filter_table(self):
        filter_text = self.lineEdit.text().lower()
        for row in range(self.tableWidget.rowCount()):
            match = False
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item and filter_text in item.text().lower():
                    match = True
                    break
            self.tableWidget.setRowHidden(row, not match)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
