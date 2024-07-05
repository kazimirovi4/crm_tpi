import sqlite3


def add_admin(login, password, level):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO admins (login, pass, level) VALUES (?, ?, ?)", (login, password, level))
    conn.commit()
    conn.close()


def add_order(Клиент_id, Товар_арт, admin_id, Статус):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Заказы (Клиент_id, Товар_арт, admin_id, Статус) VALUES (?, ?, ?, ?)",
              (Клиент_id, Товар_арт, admin_id, Статус))
    conn.commit()
    conn.close()


def add_category(Имя):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Категории (Имя) VALUES (?)", (Имя,))
    conn.commit()
    conn.close()


def add_product(Имя, Артикул, Категория_id, Характеристики, Картинка):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Товары (Имя, Артикул, Категория_id, Характеристики, Картинка) VALUES(?, ?, ?, ?, ?)",
              (Имя, Артикул, Категория_id, Характеристики, Картинка))
    conn.commit()
    conn.close()





# add_admin('admin', 'admin', 'superuser')
# add_order(1, 'LP1001', 1, 'В_пути')
# add_category('Молочная продукция')
# add_product('Молоко', 'LP1001', 1, 'Бутыла 1л', '!!!!!!!!!')

