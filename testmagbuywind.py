from PyQt5 import QtCore, QtGui, QtWidgets
#новая транзакция

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1123, 865)
        self.comboBox_1 = QtWidgets.QComboBox(Dialog)
        self.comboBox_1.setGeometry(QtCore.QRect(30, 30, 211, 31))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItems(["Перемещение", "Продажа", "Списание", "Приёмка"])

        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(250, 30, 211, 31))
        self.label_1.setObjectName("label_1")
        self.label_1.setText("Тип операции")

        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 70, 211, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["Склад 1", "Склад 2", "Склад 3", "Со всех складов"])

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 70, 211, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Склад откуда")

        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(30, 110, 211, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(["Склад 1", "Склад 2", "Склад 3"])

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 110, 211, 31))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Склад куда")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 150, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 200, 581, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(670, 270, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 270, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 310, 1051, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setHorizontalHeaderLabels([
            "Артикул", "Наименование", "Категория", "Характеристики", "Срок годности",
            "Картинка", "Количество на складах", "Цена за единицу", "Количество заказа"
        ])

        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 610, 1051, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(2)
        self.tableWidget_2.setHorizontalHeaderLabels([
            "Артикул", "Наименование", "Категория", "Характеристики", "Срок годности",
            "Картинка", "Количество", "Цена за единицу", "Сумма"
        ])

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 820, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(990, 820, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 240, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(920, 210, 71, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(1010, 210, 71, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(860, 220, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(930, 240, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(1020, 240, 31, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(990, 270, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(270, 810, 391, 41))
        self.checkBox.setObjectName("checkBox")

        self.lineEdit.setPlaceholderText("Ответственное лицо")
        self.lineEdit_2.setPlaceholderText("Фильтр")
        self.lineEdit_3.setPlaceholderText("От")
        self.lineEdit_4.setPlaceholderText("До")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.resize_table_columns(self.tableWidget)
        self.resize_table_columns(self.tableWidget_2)
        self.lineEdit_2.textChanged.connect(self.filter_table)
        self.pushButton_5.clicked.connect(self.filter_by_price)

    def resize_table_columns(self, table):
        table.resizeColumnsToContents()
        min_width = table.columnWidth(0)
        for col in range(table.columnCount()):
            table.setColumnWidth(col, max(min_width, table.columnWidth(col)))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Обновить"))
        self.pushButton_2.setText(_translate("Dialog", "Поиск"))
        self.pushButton_3.setText(_translate("Dialog", "Отмена"))
        self.pushButton_4.setText(_translate("Dialog", "Сохранить"))
        self.label_2.setText(_translate("Dialog", "Цена"))
        self.pushButton_5.setText(_translate("Dialog", "Поиск"))
        self.checkBox.setText(_translate("Dialog", "Хотите ли вы просмотреть счет после сохранения операции?"))


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

    def filter_by_price(self):
        min_price_text = self.lineEdit_3.text()
        max_price_text = self.lineEdit_4.text()

        min_price = float(min_price_text) if min_price_text else None
        max_price = float(max_price_text) if max_price_text else None

        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 6)
            if item:
                try:
                    price = float(item.text())
                    hide_row = False
                    if (min_price is not None and price < min_price) or (max_price is not None and price > max_price):
                        hide_row = True
                    self.tableWidget.setRowHidden(row, hide_row)
                except ValueError:
                    self.tableWidget.setRowHidden(row, True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
