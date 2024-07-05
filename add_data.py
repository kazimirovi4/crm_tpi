import sqlite3




orders_insert = "INSERT OR IGNORE INTO Заказы (Клиент_id, Товар_арт, admin_id, Дата_создания, Статус) values(?, ?, ?, ?, ?)"
categories_insert = "INSERT OR IGNORE INTO Категории (Имя) values(?)"

def add_admin(login, password, level):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO admins (login, pass, level) VALUES (?, ?, ?)", (login, password, level))
    conn.commit()
    conn.close()

def add_order(Клиент_id, Товар_арт, admin_id, Статус):
    conn = sqlite3.connect('crm.db')
    c = conn.cursor()
    c.execute("INSERT INTO Заказы (Клиент_id, Товар_арт, admin_id, Статус) VALUES (?, ?, ?, ?)", (Клиент_id, Товар_арт, admin_id, Статус))
    conn.commit()
    conn.close()

add_admin('admin', 'admin', 'superuser')
add_order(1, 'LP1001', 1, 'В_пути')
