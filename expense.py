import sqlite3
from datetime import date

def add_expense(item, amount):
    conn = sqlite3.connect("student.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO expenses(item,amount,date) VALUES(?,?,?)",
        (item, amount, str(date.today()))
    )
    conn.commit()
    conn.close()