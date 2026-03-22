import sqlite3

def add_expense(user_id,item,category,amount,date,time):

    conn = sqlite3.connect("student.db")
    c = conn.cursor()

    c.execute(
    "INSERT INTO expenses(user_id,item,category,amount,date,time) VALUES(?,?,?,?,?,?)",
    (user_id,item,category,amount,date,time)
    )

    conn.commit()
    conn.close()