import sqlite3 as sql
import os

C = os.path.dirname(__file__)
print(C)
conn = sql.connect(f'{C}/userdata.db')
print('생성')

conn.execute(
    '''
    create table userdata (id integer primary key, name text, email text, password text, ticket text)
    '''
)

conn.close()

with sql.connect(C+'/userdata.db') as con:
    cur = con.cursor()
    cur.execute(
        'INSERT INTO userdata (name, email, password, ticket) VALUES (?,?,?,?)',
        ("조승완", 'swan823@naver.com', "qwerty", "none"))
    print('end')
    con.commit()