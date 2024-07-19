import sqlite3
connection = sqlite3.connect('data.db')
with open('init_db.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
connection.commit()
connection.close()