import sqlite3

conn = sqlite3.connect("student.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
item TEXT,
amount REAL,
date TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS time_logs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
activity TEXT,
hours REAL,
date TEXT
)
""")

conn.commit()
conn.close()

print("Database ready!")