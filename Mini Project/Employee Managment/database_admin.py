import sqlite3

con = sqlite3.connect("database_admin.db")
data = con.cursor()

def select():
    data.execute("SELECT * FROM Administrator")
    result = data.fetchall()
    return result

def update(username,password):
    data.execute(f'UPDATE Administrator SET username="{username}",password="{password}"')
    con.commit()