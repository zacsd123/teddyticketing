import sqlite3 as sql
import os

C = os.path.dirname(__file__)
print(C)
conn = sql.connect(f'{C}/ticketdata.db')
print('생성')

conn.execute(
    '''
    create table ticket (id integer primary key, row text, column int, value text)
    '''
)

conn.close()

with sql.connect(C+'/ticketdata.db') as con:
    cur = con.cursor()
    for row in "ABCDEFGHIJKLMNOPQ":
        for column in range(13):
            if column == 6:
                cur.execute(
                    'INSERT INTO ticket (row, column, value) VALUES (?,?,?)',
                    (row, column, "Null"))
            else:
                cur.execute(
                    'INSERT INTO ticket (row, column, value) VALUES (?,?,?)',
                    (row, column, "0"))
    print('end')
    con.commit()

