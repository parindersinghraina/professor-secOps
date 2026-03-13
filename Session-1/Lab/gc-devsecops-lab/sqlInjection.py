import sqlite3

def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # NOW Semgrep will flag this — query is actually executed
    cursor.execute("SELECT * FROM users WHERE id = " + user_id)
    return cursor.fetchall()