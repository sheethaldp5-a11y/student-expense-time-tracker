import sqlite3

def register_user(username,password):

    conn = sqlite3.connect("student.db")
    c = conn.cursor()

    try:
        c.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username,password)
        )

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()


def login_user(username,password):

    conn = sqlite3.connect("student.db")
    c = conn.cursor()

    c.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username,password)
    )

    data = c.fetchone()

    conn.close()

    return data