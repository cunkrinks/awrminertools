import sqlite3


conn = sqlite3.connect('my_database.db') # Connects to or creates 'my_database.db'
cursor = conn.cursor()
#cursor.execute('''
#        CREATE TABLE IF NOT EXISTS users (
#            id INTEGER PRIMARY KEY,
#            name TEXT,
#            age INTEGER
#        )
#    ''')
conn.commit()
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("bwok", 45))
conn.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()