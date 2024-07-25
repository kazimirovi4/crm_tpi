from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import openpyxl
from add_data import handle_transfer, handle_sale_or_writeoff, handle_reception


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1120, 950)
        self.comboBox_1 = QtWidgets.QComboBox(Dialog)
        self.comboBox_1.setGeometry(QtCore.QRect(30, 30, 211, 31))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItems(["Перемещение", "Продажа", "Списание", "Приёмка", " "])
        self.comboBox_1.setCurrentIndex(-1)

        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(250, 30, 211, 31))
        self.label_1.setObjectName("label_1")
        self.label_1.setText("Тип операции")

        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 70, 211, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["Склад 1", "Склад 2", "Склад 3", "Со всех складов", " "])
        self.comboBox_2.setCurrentIndex(-1)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 70, 211, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Склад откуда")

        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(30, 110, 211, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(["Склад 1", "Склад 2", "Склад 3", " "])
        self.comboBox_3.setCurrentIndex(-1)

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
        self.pushButton.clicked.connect(self.refresh_data)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 310, 1051, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setHorizontalHeaderLabels([
            "Артикул", "Наименование", "Цена", "Категория", "Характеристики", "Картинка", "Склад",
            "Количество на складах"
        ])

        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 610, 1051, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setHorizontalHeaderLabels([
            "Артикул", "Наименование", "Цена", "Категория", "Характеристики", "Картинка", "Склад",
            "Количество на складах", "Итоговая цена"
        ])

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 870, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.cancel_action)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(990, 870, 93, 28))
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
        self.checkBox.setGeometry(QtCore.QRect(270, 860, 391, 41))
        self.checkBox.setObjectName("checkBox")

        self.total_label = QtWidgets.QLabel(Dialog)
        self.total_label.setGeometry(QtCore.QRect(830, 810, 300, 50))
        self.total_label.setObjectName("total_label")
        self.total_label.setText("Итоговая стоимость: 0")
        self.total_label.setStyleSheet("font-size: 16px;")

        self.lineEdit_2.setPlaceholderText("Фильтр")
        self.lineEdit_3.setPlaceholderText("От")
        self.lineEdit_4.setPlaceholderText("До")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 150, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("admin")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.resize_table_columns(self.tableWidget)
        self.resize_table_columns(self.tableWidget_2)
        self.lineEdit_2.textChanged.connect(self.filter_table)
        self.pushButton_5.clicked.connect(self.filter_by_price)
        self.comboBox_2.currentIndexChanged.connect(self.filter_by_warehouse)
        self.load_data()
        self.tableWidget.cellDoubleClicked.connect(self.copy_to_tableWidget_2)
        self.pushButton_4.clicked.connect(self.save_data)
        self.comboBox_1.currentIndexChanged.connect(self.update_ui_based_on_operation)

        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(450, 30, 211, 31))
        self.comboBox_4.setObjectName("comboBox_4")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(670, 30, 211, 31))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Клиент")
        self.load_clients()


    def resize_table_columns(self, table):
        table.resizeColumnsToContents()
        min_width = table.columnWidth(0)
        for col in range(table.columnCount()):
            table.setColumnWidth(col, max(min_width, table.columnWidth(col)))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Обновить"))

        self.pushButton_3.setText(_translate("Dialog", "Отмена"))
        self.pushButton_4.setText(_translate("Dialog", "Сохранить"))
        self.label_2.setText(_translate("Dialog", "Цена"))
        self.pushButton_5.setText(_translate("Dialog", "Поиск"))
        self.checkBox.setText(_translate("Dialog", "Хотите ли вы просмотреть счет после сохранения операции?"))

    def load_data(self):
        conn = sqlite3.connect('crm.db')
        c = conn.cursor()

        c.execute('''
            SELECT Products.art, Products.name, Products.price, Categories.name, Products.characteristics, Products.picture, 
            Warehouses.name, Product_Warehouse.quantity
            FROM Products
            JOIN Categories ON Products.category_id = Categories.id
            JOIN Warehouses ON Product_Warehouse.warehouse_id = Warehouses.id
            JOIN Product_Warehouse ON Products.id = Product_Warehouse.product_id
            ''')
        rows = c.fetchall()
        conn.close()

        self.tableWidget.setRowCount(len(rows))

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_num, col_num, item)

    def load_clients(self):
        conn = sqlite3.connect('crm.db')
        c = conn.cursor()
        c.execute('SELECT id, full_name FROM Clients')
        clients = c.fetchall()
        for client_id, client_name in clients:
            self.comboBox_4.addItem(client_name, client_id)
            self.comboBox_4.setCurrentIndex(-1)
        conn.close()



    def copy_to_tableWidget_2(self, row, column):
        row_data = []
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, col)
            row_data.append(item.text() if item else "")

        quantity_dialog = QtWidgets.QInputDialog()
        quantity_dialog.setInputMode(QtWidgets.QInputDialog.IntInput)
        quantity_dialog.setWindowTitle("Введите количество")
        quantity_dialog.setLabelText("Количество:")
        quantity_dialog.setIntRange(1, int(row_data[7]))

        if quantity_dialog.exec_() == QtWidgets.QDialog.Accepted:
            quantity = quantity_dialog.intValue()
            current_quantity = int(row_data[7])
            new_quantity = current_quantity - quantity

            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(new_quantity)))

            row_data[7] = str(quantity)

            total_price = float(row_data[2]) * quantity
            row_data.append(str(total_price))

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

            for col, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(data)
                self.tableWidget_2.setItem(row_position, col, item)

            self.update_total_price()

    def update_total_price(self):
        total = 0
        for row in range(self.tableWidget_2.rowCount()):
            item = self.tableWidget_2.item(row, 8)
            if item:
                try:
                    total += float(item.text())
                except ValueError:
                    pass
        self.total_label.setText(f"Итоговая стоимость: {total} BYN")

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

    def filter_by_price(self):
        min_price_text = self.lineEdit_3.text()
        max_price_text = self.lineEdit_4.text()

        min_price = float(min_price_text) if min_price_text else None
        max_price = float(max_price_text) if max_price_text else None

        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 2)
            if item:
                try:
                    price = float(item.text())
                    hide_row = False
                    if (min_price is not None and price < min_price) or (max_price is not None and price > max_price):
                        hide_row = True
                    self.tableWidget.setRowHidden(row, hide_row)
                except ValueError:
                    self.tableWidget.setRowHidden(row, True)

    def filter_by_warehouse(self):
        selected_warehouse = self.comboBox_2.currentText()
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 6)
            if selected_warehouse == "Со всех складов":
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, item.text() != selected_warehouse)

    def save_to_excel(self):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Данные"

        headers = [self.tableWidget_2.horizontalHeaderItem(col).text() for col in
                   range(self.tableWidget_2.columnCount())]
        ws.append(headers)

        for row in range(self.tableWidget_2.rowCount()):
            row_data = [self.tableWidget_2.item(row, col).text() if self.tableWidget_2.item(row, col) else "" for col in
                        range(self.tableWidget_2.columnCount())]
            ws.append(row_data)

        total_row = [''] * (self.tableWidget_2.columnCount() - 1) + ["Итоговая стоимость:",
                                                                     self.total_label.text().split(': ')[1]]
        ws.append(total_row)

        wb.save("output.xlsx")


    def save_data(self):
        operation_type = self.comboBox_1.currentText()

        if operation_type == "Перемещение":
            handle_transfer(self.comboBox_2, self.comboBox_3, self.tableWidget_2)
        elif operation_type == "Продажа":
            handle_sale_or_writeoff(self.comboBox_2, self.tableWidget_2)
        elif operation_type == "Списание":
            handle_sale_or_writeoff(self.comboBox_2, self.tableWidget_2)
        elif operation_type == "Приёмка":
            handle_reception(self.comboBox_3, self.tableWidget_2)

        if self.checkBox.isChecked():
            self.save_to_excel()

        self.save_orders_to_database()
        QtWidgets.QMessageBox.information(None, "Сохранение", "Данные успешно сохранены и обновлены в базе данных.")

    def get_current_admin_id(self):
        return self.lineEdit.text()

    def save_orders_to_database(self):
        conn = sqlite3.connect('crm.db')
        c = conn.cursor()

        client_id = self.comboBox_4.currentData()
        admin_id = '1'

        for row in range(self.tableWidget_2.rowCount()):
            art = self.tableWidget_2.item(row, 0).text()

            c.execute('''
                INSERT INTO Orders (client_id, product_art, admin_id, status)
                VALUES (?, ?, ?, ?)
            ''', (client_id, art, admin_id, "New"))

        conn.commit()
        conn.close()

    def update_ui_based_on_operation(self):
        operation_type = self.comboBox_1.currentText()

        if operation_type == "Перемещение":
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(True)
            self.comboBox_4.setEnabled(False)
            self.comboBox_2.setCurrentIndex(-1)
            self.comboBox_3.setCurrentIndex(-1)
        elif operation_type == "Продажа":
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(False)
            self.comboBox_4.setEnabled(True)
            self.comboBox_2.setCurrentIndex(-1)
            self.comboBox_3.setCurrentIndex(-1)
        elif operation_type == "Списание":
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(False)
            self.comboBox_4.setEnabled(False)
            self.comboBox_2.setCurrentIndex(-1)
            self.comboBox_3.setCurrentIndex(-1)
        elif operation_type == "Приёмка":
            self.comboBox_2.setEnabled(False)
            self.comboBox_3.setEnabled(True)
            self.comboBox_4.setEnabled(False)
            self.comboBox_2.setCurrentIndex(-1)
            self.comboBox_3.setCurrentIndex(-1)
        else:
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(True)
            self.comboBox_4.setEnabled(False)
            self.comboBox_2.setCurrentIndex(-1)
            self.comboBox_3.setCurrentIndex(-1)

    def refresh_data(self):
        self.tableWidget.clearContents()
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)
        self.load_data()

    def cancel_action(self):
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)
        self.load_data()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
