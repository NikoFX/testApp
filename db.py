import sqlite3

### Connect DB
conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY,
    unit TEXT NOT NULL,
    speed INTEGER NOT NULL,
    location TEXT NOT NULL,
    recordTime TEXT NOT NULL,
    googleLink TEXT NOT NULL,
    date DATETIME NOT NULL,
    read INTEGER NOT NULL
)
''')

conn.commit()

### End Connect DB