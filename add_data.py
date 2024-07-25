import sqlite3
import uuid



def get_category_id(category_name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT id FROM Categories WHERE name = ?", (category_name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


def add_category(category_name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Categories (name) VALUES (?)", (category_name,))
    conn.commit()
    category_id = c.lastrowid
    conn.close()
    return category_id


def generate_unique_article():
    return str(uuid.uuid4())


def add_product(name, category_name, price, characteristics, image, sklad_id):
    category_id = get_category_id(category_name)
    if not category_id:
        category_id = add_category(category_name)
    article = generate_unique_article()
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Products (name, art, category_id, price, characteristics, picture, warehouse_id) VALUES(?, ?, ?, ?, ?, ?, ?)",
              (name, article, category_id, price, characteristics, image, sklad_id))
    conn.commit()
    conn.close()


def add_warehouse(name, address, coordinates):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Warehouses (name, address, coordinates) VALUES (?, ?, ?)",
              (name, address, coordinates))
    conn.commit()
    conn.close()


def get_warehouse_id(warehouse_name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT id FROM Warehouses WHERE name = ?", (warehouse_name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


def add_client(full_name, address, phone):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Clients (full_name, address, phone) VALUES (?, ?, ?)",
              (full_name, address, phone))
    conn.commit()
    conn.close()


def add_document(name, type, creation_date, content):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Documents (name, type, date, content) VALUES (?, ?, ?, ?)",
              (name, type, creation_date, content))
    conn.commit()
    conn.close()


def get_client_id(client_name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT id FROM Clients WHERE full_name = ?", (client_name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


def get_product_article(product_name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT art FROM Products WHERE name = ?", (product_name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


def get_product_id(product_name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT id FROM Products WHERE name = ?", (product_name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


def add_admin(login, password, level):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO admins (login, pass, level) VALUES (?, ?, ?)", (login, password, level))
    conn.commit()
    conn.close()

def get_admin_id(admin_login):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT id FROM admins WHERE login = ?", (admin_login,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


def add_order(client_name, product_name, admin_login, status):
    client_id = get_client_id(client_name)
    product_article = get_product_article(product_name)
    admin_id = get_admin_id(admin_login)
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Orders (client_id, product_art, admin_id, status) VALUES (?, ?, ?, ?)",
              (client_id, product_article, admin_id, status))
    conn.commit()
    conn.close()

def add_warehouse_product(product_name, warehouse_name, quantity):
    product_id = get_product_id(product_name)
    warehouse_id = get_warehouse_id(warehouse_name)
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Product_Warehouse (product_id, warehouse_id, quantity) VALUES (?, ?, ?)",
              (product_id, warehouse_id, quantity))
    conn.commit()
    conn.close()

def handle_transfer(comboBox_2, comboBox_3, tableWidget_2):
    warehouse_from = comboBox_2.currentText()
    warehouse_to = comboBox_3.currentText()

    conn = sqlite3.connect('crm.db')
    c = conn.cursor()

    for row in range(tableWidget_2.rowCount()):
        art = tableWidget_2.item(row, 0).text()
        quantity = int(tableWidget_2.item(row, 7).text())

        c.execute('''
            UPDATE Product_Warehouse
            SET quantity = quantity - ?
            WHERE product_id = (SELECT id FROM Products WHERE art = ?) AND warehouse_id = (SELECT id FROM Warehouses WHERE name = ?)
        ''', (quantity, art, warehouse_from))

        c.execute('''
            SELECT quantity FROM Product_Warehouse
            WHERE product_id = (SELECT id FROM Products WHERE art = ?) AND warehouse_id = (SELECT id FROM Warehouses WHERE name = ?)
        ''', (art, warehouse_to))

        result = c.fetchone()

        if result:
            c.execute('''
                UPDATE Product_Warehouse
                SET quantity = quantity + ?
                WHERE product_id = (SELECT id FROM Products WHERE art = ?) AND warehouse_id = (SELECT id FROM Warehouses WHERE name = ?)
            ''', (quantity, art, warehouse_to))
        else:
            c.execute('''
                INSERT INTO Product_Warehouse (product_id, warehouse_id, quantity)
                VALUES ((SELECT id FROM Products WHERE art = ?), (SELECT id FROM Warehouses WHERE name = ?), ?)
            ''', (art, warehouse_to, quantity))

    conn.commit()
    conn.close()

def handle_sale_or_writeoff(comboBox_2, tableWidget_2):
    warehouse_from = comboBox_2.currentText()

    conn = sqlite3.connect('crm.db')
    c = conn.cursor()

    for row in range(tableWidget_2.rowCount()):
        art = tableWidget_2.item(row, 0).text()
        quantity = int(tableWidget_2.item(row, 7).text())

        if warehouse_from == "Со всех складов":
            warehouses = tableWidget_2.item(row, 6).text().split(',')
            for warehouse in warehouses:
                c.execute('''
                        UPDATE Product_Warehouse
                        SET quantity = quantity - ?
                        WHERE product_id = (SELECT id FROM Products WHERE art = ?) AND warehouse_id = (SELECT id FROM Warehouses WHERE name = ?)
                    ''', (quantity, art, warehouse.strip()))
        else:
            c.execute('''
                    UPDATE Product_Warehouse
                    SET quantity = quantity - ?
                    WHERE product_id = (SELECT id FROM Products WHERE art = ?) AND warehouse_id = (SELECT id FROM Warehouses WHERE name = ?)
                ''', (quantity, art, warehouse_from))

    conn.commit()
    conn.close()

def handle_reception(comboBox_3, tableWidget_2):
    warehouse_to = comboBox_3.currentText()

    conn = sqlite3.connect('crm.db')
    c = conn.cursor()

    for row in range(tableWidget_2.rowCount()):
        art = tableWidget_2.item(row, 0).text()
        additional_quantity = int(tableWidget_2.item(row, 7).text())

        c.execute('''
            SELECT id, quantity
            FROM Product_Warehouse
            WHERE product_id = (SELECT id FROM Products WHERE art = ?) AND warehouse_id = (SELECT id FROM Warehouses WHERE name = ?)
        ''', (art, warehouse_to))
        result = c.fetchone()

        if result:
            current_quantity = result[1]
            new_quantity = current_quantity + additional_quantity
            c.execute('''
                UPDATE Product_Warehouse
                SET quantity = ?
                WHERE id = ?
            ''', (new_quantity, result[0]))
        else:
            c.execute('''
                INSERT INTO Product_Warehouse (product_id, warehouse_id, quantity)
                VALUES ((SELECT id FROM Products WHERE art = ?), (SELECT id FROM Warehouses WHERE name = ?), ?)
            ''', (art, warehouse_to, additional_quantity))

    conn.commit()
    conn.close()

def update_database_buywind(tableWidget):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()

    for row in range(tableWidget.rowCount()):
        art = tableWidget.item(row, 0).text()
        quantity = tableWidget.item(row, 7).text()

        c.execute('''
            UPDATE Product_Warehouse
            SET quantity = ?
            WHERE product_id = (SELECT id FROM Products WHERE art = ?)
        ''', (quantity, art))

    conn.commit()
    conn.close()