from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from add_data import add_product, add_warehouse, add_client, add_document


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
        self.pushButton.clicked.connect(self.load_data)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 310, 1051, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID Товара", "Наименование товара", "Артикул", "Категория", "Характеристики", "Картинка"
        ])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 610, 1051, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setHorizontalHeaderLabels([
            "Наименование товара", "Категория", "Характеристики", "Картинка"
        ])
        header_2 = self.tableWidget_2.horizontalHeader()
        header_2.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 820, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.load_data()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Обновить"))
        self.pushButton_3.setText(_translate("Dialog", "Отмена"))
        self.pushButton_4.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_5.setText(_translate("Dialog", "Удалить строку"))

    def updateTables(self):
        self.load_data()

    def load_data(self):
        index = self.comboBox.currentIndex()
        conn = sqlite3.connect('crm.db')
        c = conn.cursor()

        if index == 0:
            c.execute('SELECT * FROM Товары')
            columns = ["ID Товара", "Наименование товара", "Артикул", "Категория", "Характеристики", "Картинка"]
            columns_2 = ["Наименование товара", "Категория", "Характеристики", "Картинка"]
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

        rows = c.fetchall()

        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

        self.tableWidget_2.setColumnCount(len(columns_2))
        self.tableWidget_2.setHorizontalHeaderLabels(columns_2)
        self.tableWidget_2.setRowCount(1)
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
            add_product(data[0], data[1], data[2], data[3])
        elif index == 1:
            add_warehouse(data[0], data[1], data[2])
        elif index == 2:
            add_client(data[0], data[1], data[2])
        elif index == 3:
            add_document(data[0], data[1], data[2], data[3])

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
