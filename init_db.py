import sqlite3
import json
connection = sqlite3.connect('data.db')

try:
   with open('init_db.sql', 'r') as f:
      contents = f.read()
      connection.executescript(contents)
except Exception:
   exit(0)

score = []
with open('yt2-sorted-2.json') as f:
   scores = json.load(f)


cur = connection.cursor()
for score in scores:
   name = score.get('Name')
   ID = score.get('ID')
   Van = score.get('Van')
   Anh = score.get('Anh')
   Toan = score.get('Toan')
   Tong = score.get('Tong')
   Rank = score.get('Rank')
   cur.execute("INSERT INTO scores VALUES (?, ?, ?, ?, ?, ?, ?)",
            (name, ID, Van, Anh, Toan, Tong, Rank)
            )


connection.commit()
connection.close()