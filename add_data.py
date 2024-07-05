import sqlite3


conn = sqlite3.connect('crm.db')
c = conn.cursor()



conn.commit()
conn.close()