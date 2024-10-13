import sqlite3
import routes

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS User (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
famil TEXT NOT NULL,
age INTEGER
)
''')

con.commit()

def f(id, name, famil, age):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("INSERT INTO User VALUES(?, ?, ?, ?)", (id, name, famil, age))
    con.commit()

def get_f():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM User")
    return res.fetchall()
    con.commit()




