from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1123, 865)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 60, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Товар", "Склад", "Клиент", "Документы"])
        self.comboBox.currentIndexChanged.connect(self.updateTables)

        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(250, 60, 211, 31))
        self.label_1.setObjectName("label_1")
        self.label_1.setText("Что добавляем")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 120, 211, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 200, 581, 51))
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
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setHorizontalHeaderLabels([
            "Артикул", "Наименование", "Категория", "Характеристики","Картинка", "Количество заказа"
        ])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 610, 1051, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setHorizontalHeaderLabels([
            "Наименование", "Категория", "Характеристики", "Картинка", "Количество заказа"
        ])
        header_2 = self.tableWidget_2.horizontalHeader()
        header_2.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 820, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(990, 820, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 220, 55, 16))
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(922, 270, 131, 28))
        self.pushButton_5.setObjectName("pushButton_5")

        self.lineEdit.setPlaceholderText("Ответственное лицо")
        self.lineEdit_2.setPlaceholderText("Фильтр")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Обновить"))
        self.pushButton_2.setText(_translate("Dialog", "Поиск"))
        self.pushButton_3.setText(_translate("Dialog", "Отмена"))
        self.pushButton_4.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_5.setText(_translate("Dialog", "Удалить строку"))

    def updateTables(self):
        index = self.comboBox.currentIndex()
        if index == 0:
            self.fillTableForProduct()
        elif index == 1:
            self.fillTableForWarehouse()
        elif index == 2:
            self.fillTableForClient()
        elif index == 3:
            self.fillTableForDocuments()

    def fillTableForProduct(self):
        self.tableWidget.setHorizontalHeaderLabels([
            "Артикул", "Наименование", "Категория", "Характеристики", "Картинка", "Количество заказа"
        ])
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(6)

        self.tableWidget_2.setHorizontalHeaderLabels([
            "Наименование", "Категория", "Характеристики", "Картинка", "Количество заказа"
        ])
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(5)

    def fillTableForWarehouse(self):
        self.tableWidget.setHorizontalHeaderLabels([
            "Складской номер", "Наименование", "Местоположение", "Вместимость", "Заполненность", "Ответственный"
        ])
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(6)

        self.tableWidget_2.setHorizontalHeaderLabels([
            "Наименование", "Местоположение", "Вместимость", "Заполненность", "Ответственный"
        ])
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(5)

    def fillTableForClient(self):
        self.tableWidget.setHorizontalHeaderLabels([
            "ID клиента", "Имя", "Фамилия", "Email", "Телефон", "Адрес"
        ])
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(6)

        self.tableWidget_2.setHorizontalHeaderLabels([
            "Имя", "Фамилия", "Email", "Телефон", "Адрес"
        ])
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(5)

    def fillTableForDocuments(self):
        self.tableWidget.setHorizontalHeaderLabels([
            "ID документа", "Тип", "Дата создания", "Статус", "Ответственный", "Описание"
        ])
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(6)

        self.tableWidget_2.setHorizontalHeaderLabels([
            "Тип", "Дата создания", "Статус", "Ответственный", "Описание"
        ])
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(5)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
