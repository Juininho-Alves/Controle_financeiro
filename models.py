import sqlite3


def conexao():
    conn = sqlite3.connect('database.db')
    return conn
