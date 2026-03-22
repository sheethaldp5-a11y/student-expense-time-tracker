import sqlite3

def add_time(user_id,activity,hours,date,time):

    conn = sqlite3.connect("student.db")
    c = conn.cursor()

    c.execute(
    "INSERT INTO time_logs(user_id,activity,hours,date,time) VALUES(?,?,?,?,?)",
    (user_id,activity,hours,date,time)
    )

    conn.commit()
    conn.close()