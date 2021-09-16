import sqlite3 
# Connects to store.db database, for this example we assume it already exists
connection = sqlite3.connect('store.db') 
cursor = connection.cursor()

cursor.execute('SELECT * FROM fruit')
rows = cursor.fetchall()
for row in rows:
    print(row)
