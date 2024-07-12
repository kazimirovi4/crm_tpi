from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from add_data import add_product, add_warehouse, add_client, add_document, add_warehouse_product


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1123, 865)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 60, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Товар", "Склад", "Клиент", "Документы", "Продукты на складах"])
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
        self.pushButton.clicked.connect(self.load_data)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 310, 1051, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID Товара", "Наименование товара", "Артикул", "Категория", "Характеристики", "Картинка, Склад_id"
        ])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 610, 951, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setHorizontalHeaderLabels([
            "Наименование товара", "Категория", "Характеристики", "Картинка", 'Склад_id'
        ])
        header_2 = self.tableWidget_2.horizontalHeader()
        header_2.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(990, 820, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.save_data)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 220, 55, 16))
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(922, 270, 131, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.delete_row)

        self.lineEdit.setPlaceholderText("Ответственное лицо")
        self.lineEdit_2.setPlaceholderText("Фильтр")

        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(990, 610, 93, 28))
        self.addButton.setObjectName("addButton")
        self.addButton.setText("+")
        self.addButton.clicked.connect(self.add_row)

        self.removeButton = QtWidgets.QPushButton(Dialog)
        self.removeButton.setGeometry(QtCore.QRect(990, 648, 93, 28))
        self.removeButton.setObjectName("removeButton")
        self.removeButton.setText("-")
        self.removeButton.clicked.connect(self.remove_row)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.lineEdit_2.textChanged.connect(self.filter_table)
        self.load_data()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Обновить"))
        self.pushButton_4.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_5.setText(_translate("Dialog", "Удалить строку"))
        self.addButton.setText(_translate("Dialog", "+"))
        self.removeButton.setText(_translate("Dialog", "-"))

    def filter_table(self):
        filter_text = self.lineEdit_2.text().lower()
        for row in range(self.tableWidget.rowCount()):
            match = False
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item and filter_text in item.text().lower():
                    match = True
                    break
            self.tableWidget.setRowHidden(row, not match)

    def updateTables(self):
        self.load_data()

    def load_data(self):
        index = self.comboBox.currentIndex()
        conn = sqlite3.connect('crm.db')
        c = conn.cursor()

        if index == 0:
            c.execute('SELECT * FROM Товары')
            columns = ["ID Товара", "Наименование товара", "Артикул", "Категория", "Цена", "Характеристики", "Картинка", "Склад_id"]
            columns_2 = ["Наименование товара", "Категория", "Характеристики", "Картинка", "Цена", "Склад_id"]
        elif index == 1:
            c.execute('SELECT * FROM Склады')
            columns = ["ID Склада", "Название", "Адрес", "Местоположение"]
            columns_2 = ["Название", "Адрес", "Местоположение"]
        elif index == 2:
            c.execute('SELECT * FROM Клиенты')
            columns = ["ID клиента", "ФИО", "Адрес", "Телефон"]
            columns_2 = ["ФИО", "Адрес", "Телефон"]
        elif index == 3:
            c.execute('SELECT * FROM Документы')
            columns = ["ID документа", "Название", "Тип", "Дата создания", "Описание"]
            columns_2 = ["Название", "Тип", "Дата создания", "Описание"]
        elif index == 4:
            c.execute('SELECT * FROM Товар_Склад')
            columns = ["ID", "Товар_id", "Склад_id", "Количество"]
            columns_2 = ["Товар_id", "Склад_id", "Количество"]

        rows = c.fetchall()

        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

        self.tableWidget_2.setColumnCount(len(columns_2))
        self.tableWidget_2.setHorizontalHeaderLabels(columns_2)
        self.tableWidget_2.setRowCount(0)
        for col_idx, col_data in enumerate(columns_2):
            self.tableWidget_2.setItem(0, col_idx, QtWidgets.QTableWidgetItem(""))

        conn.close()

    def save_data(self):
        index = self.comboBox.currentIndex()
        data = []
        for col in range(self.tableWidget_2.columnCount()):
            item = self.tableWidget_2.item(0, col)
            data.append(item.text() if item else '')

        if index == 0:
            add_product(data[0], data[1], data[2], data[3], data[4])
        elif index == 1:
            add_warehouse(data[0], data[1], data[2])
        elif index == 2:
            add_client(data[0], data[1], data[2])
        elif index == 3:
            add_document(data[0], data[1], data[2], data[3])
        elif index == 4:
            add_warehouse_product(data[0], data[1], data[2])

        self.load_data()

    def delete_row(self):
        index = self.comboBox.currentIndex()
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            return
        item_id = self.tableWidget.item(selected_row, 0).text()
        conn = sqlite3.connect('crm.db')
        c = conn.cursor()
        if index == 0:
            c.execute("DELETE FROM Товары WHERE ID = ?", (item_id,))
        elif index == 1:
            c.execute("DELETE FROM Склады WHERE ID = ?", (item_id,))
        elif index == 2:
            c.execute("DELETE FROM Клиенты WHERE ID = ?", (item_id,))
        elif index == 3:
            c.execute("DELETE FROM Документы WHERE ID = ?", (item_id,))
        conn.commit()
        conn.close()
        self.load_data()

    def add_row(self):
        self.tableWidget_2.insertRow(self.tableWidget_2.rowCount())

    def remove_row(self):
        current_row = self.tableWidget_2.currentRow()
        if current_row != -1:
            self.tableWidget_2.removeRow(current_row)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
