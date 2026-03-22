import sqlite3
import pandas as pd

def load_data(user_id):

    conn = sqlite3.connect("student.db")

    exp = pd.read_sql_query(
    "SELECT * FROM expenses WHERE user_id=?",
    conn,
    params=(user_id,)
    )

    time = pd.read_sql_query(
    "SELECT * FROM time_logs WHERE user_id=?",
    conn,
    params=(user_id,)
    )

    conn.close()

    return exp,time


def productivity_score(exp,time):

    study = time["hours"].sum() if not time.empty else 0
    expense = exp["amount"].sum() if not exp.empty else 0

    score = study*10 - expense*0.1

    return round(score,2)