import sqlite3
from datetime import date

def add_time(activity, hours):
    conn = sqlite3.connect("student.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO time_logs(activity,hours,date) VALUES(?,?,?)",
        (activity, hours, str(date.today()))
    )
    conn.commit()
    conn.close()