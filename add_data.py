import sqlite3
import uuid


def get_category_id(category_name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT id FROM Категории WHERE Имя = ?", (category_name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


def add_category(category_name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Категории (Имя) VALUES (?)", (category_name,))
    conn.commit()
    category_id = c.lastrowid
    conn.close()
    return category_id


def generate_unique_article():
    return str(uuid.uuid4())


def add_product(name, category_name, characteristics, image, sklad_id):
    category_id = get_category_id(category_name)
    if not category_id:
        category_id = add_category(category_name)
    article = generate_unique_article()
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Товары (Имя, Артикул, Категория_id, Характеристики, Картинка, Склад_id) VALUES(?, ?, ?, ?, ?, ?)",
              (name, article, category_id, characteristics, image, sklad_id))
    conn.commit()
    conn.close()


def add_warehouse(name, address, coordinates):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Склады (Название, Адрес, Координаты) VALUES (?, ?, ?)",
              (name, address, coordinates))
    conn.commit()
    conn.close()


def add_client(full_name, address, phone):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Клиенты (ФИО, Адрес, Телефон) VALUES (?, ?, ?)",
              (full_name, address, phone))
    conn.commit()
    conn.close()


def add_document(name, type, creation_date, content):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Документы (Название, Тип, Дата_создания, Содержание) VALUES (?, ?, ?, ?)",
              (name, type, creation_date, content))
    conn.commit()
    conn.close()


def get_client_id(client_name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT id FROM Клиенты WHERE ФИО = ?", (client_name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None


def get_product_article(product_name):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("SELECT Артикул FROM Товары WHERE Имя = ?", (product_name,))
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
    c.execute("INSERT INTO Заказы (Клиент_id, Товар_арт, admin_id, Статус) VALUES (?, ?, ?, ?)",
              (client_id, product_article, admin_id, status))
    conn.commit()
    conn.close()

# add_product('Телефон', 'Электроника', '4GB RAM, 64GB ROM', 'phone.jpg')
# add_admin('admin', 'admin', 'superuser')
# add_order('Johan', 'Молоко', 'admin', 'В_пути')
# add_category('Молочная продукция')
# add_product('Молоко', 'Молочная продукция', 'бутылка', '1.jpg', '1')
# add_product('Телефон', 'Электроника', '4GB RAM, 64GB ROM', 'phone.jpg')
# add_order('Johan', 'Телефон', 'admin', 'Создан')
# add_client('Johan', 'Moscow', '+375298888888')