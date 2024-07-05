import sqlite3



conn = sqlite3.connect('crm.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS admins
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, login VARCHAR , pass VARCHAR, level VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Категории
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, Имя VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Товары
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, Имя VARCHAR, Артикул VARCHAR, Категория_id INTEGER, Характеристики VARCHAR, Картинка VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Склады
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, Название VARCHAR , Адрес VARCHAR, Координаты VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Клиенты
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, ФИО VARCHAR, Адрес VARCHAR, Телефон VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Заказы
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, Клиент_id VARCHAR, Название VARCHAR, admin_id VARCHAR, Дата_создания DATETIME, Статус VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Документы
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, Название VARCHAR, Тип VARCHAR, Дата_создания DATETIME, Содержание VARCHAR)''')

conn.commit()
conn.close()