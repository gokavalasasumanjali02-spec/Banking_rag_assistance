import sqlite3
def save_chat(
        username,
        question,
        answer
):
    conn=sqlite3.connect(
        "database/chat_hisory.db"
    )
    cur=conn.cursor()
    cur.execute("""
    INSERT INTO chat_history
    (
        username,question,answer
    )
    VALUES
    (   
        ?,
        ?,
        ?
    )
    """,
    (
        username,
        question,
        answer
    ))
    conn.commit()
