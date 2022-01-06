import sqlite3
con = sqlite3.connect("database.db")
data = con.cursor()

def select():
    data.execute("SELECT * FROM employment")
    result = data.fetchall()
    return result

def delete(i):
    data.execute(f'DELETE FROM employment WHERE frist_name = "{i}"')
    con.commit()

def add(frist_name,last_name,n_code,b_date,e_date,phone_number,pic):
    data.execute(f'INSERT INTO employment(frist_name,last_name,n_code,b_date,e_date,phone_number,img) VALUES ("{frist_name}","{last_name}","{n_code}","{b_date}","{e_date}","{phone_number}","{pic}")')
    con.commit()

def update(frist_name,last_name,n_code,b_date,e_date,phone_number,i):
    data.execute(f'UPDATE employment SET frist_name="{frist_name}",last_name="{last_name}",n_code="{n_code}",b_date="{b_date}",e_date="{e_date}",phone_number="{phone_number}",img="pics/{n_code}.jpg" WHERE n_code="{i}"')
    con.commit()