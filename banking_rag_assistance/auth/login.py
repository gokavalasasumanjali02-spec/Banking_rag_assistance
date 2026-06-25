import sqlite3

def authenticate(username, password):
    conn = sqlite3.connect("database/users.db")
    cur = conn.cursor()

    cur.execute(
        """
        SELECT password, role
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cur.fetchone()
    conn.close()

    if user:
        db_password, role = user

        if password == db_password:
            return role

    return None