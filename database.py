import sqlite3

conn = sqlite3.connect("student.db")
c = conn.cursor()

# users table
c.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
password TEXT
)
""")

# expenses table
c.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
item TEXT,
category TEXT,
amount REAL,
date TEXT,
time TEXT
)
""")

# time logs table
c.execute("""
CREATE TABLE IF NOT EXISTS time_logs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
activity TEXT,
hours REAL,
date TEXT,
time TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")