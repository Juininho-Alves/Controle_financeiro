import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    with open('schemas.sql', 'r', encoding='utf-8') as arquivo:
        conn.executescript(arquivo.read())
        conn.commit()
        conn.close()


init_db()


