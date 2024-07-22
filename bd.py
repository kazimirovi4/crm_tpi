import sqlite3




conn = sqlite3.connect('crm.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS admins
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, login VARCHAR UNIQUE, pass VARCHAR, level VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Categories
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, art VARCHAR UNIQUE,
                 category_id INTEGER, price REAL, characteristics VARCHAR, picture VARCHAR, warehouse_id VARCHAR,
                 FOREIGN KEY(category_id) REFERENCES Categories(id), FOREIGN KEY(warehouse_id) REFERENCES Warehouses(id))''')

c.execute('''CREATE TABLE IF NOT EXISTS Warehouses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR , address VARCHAR, coordinates VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Clients
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, full_name VARCHAR, address VARCHAR, phone VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Orders
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, client_id VARCHAR, product_art VARCHAR, admin_id VARCHAR, 
                 date DEFAULT CURRENT_DATE, time DEFAULT CURRENT_TIME, status VARCHAR, FOREIGN KEY(client_id) REFERENCES Clients(id), 
                 FOREIGN KEY(admin_id) REFERENCES admins(id), FOREIGN KEY(product_art) REFERENCES Products(art))''')

c.execute('''CREATE TABLE IF NOT EXISTS Documents
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, type VARCHAR, date DEFAULT CURRENT_DATE, 
                 content VARCHAR)''')

c.execute('''CREATE TABLE IF NOT EXISTS Product_Warehouse
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, product_id VARCHAR, warehouse_id VARCHAR, quantity INTEGER,
                 FOREIGN KEY(product_id) REFERENCES Products(id), FOREIGN KEY(warehouse_id) REFERENCES Warehouses(id))''')

conn.commit()
conn.close()