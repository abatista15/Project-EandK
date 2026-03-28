import sqlite3
connection = sqlite3.connect('MTG.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM Users")
results = cursor.fetchall()
for i in results:
    print(i)
    
connection.close()