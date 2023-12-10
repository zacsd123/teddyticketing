import sqlite3 as sql
import os

C = os.path.dirname(__file__)
db_path = os.path.join(C, "database")

def UserData():
    with sql.connect(db_path+"/userdata.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from userdata")
        userdata = cur.fetchall()
    return userdata

def TicketData():
    with sql.connect(db_path+"/ticketdata.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from ticket")
        ticketdata = cur.fetchall()
    return ticketdata