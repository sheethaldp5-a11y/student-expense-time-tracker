import pandas as pd
import sqlite3

def load_data():
    conn = sqlite3.connect("student.db")
    expenses = pd.read_sql("SELECT * FROM expenses", conn)
    time = pd.read_sql("SELECT * FROM time_logs", conn)
    conn.close()
    return expenses, time

def productivity_score(expenses, time):
    total_spend = expenses["amount"].sum() if not expenses.empty else 0

    waste_time = time[time["activity"].isin(
        ["social media","scrolling","gaming","youtube"]
    )]["hours"].sum()

    study_time = time[time["activity"].isin(
        ["study","class","learning"]
    )]["hours"].sum()

    score = study_time*10 - waste_time*5 - total_spend*0.05
    return round(score,2)