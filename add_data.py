import sqlite3


conn = sqlite3.connect('crm.db')
c = conn.cursor()

print('dfd')

conn.commit()
conn.close()