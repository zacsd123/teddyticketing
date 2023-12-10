from flask import Blueprint, request, session, redirect, render_template
import sqlite3 as sql
from Data import UserData, TicketData, db_path

ticketing = Blueprint("ticketing", __name__, template_folder="templates")
place = {"0":[0, 1, 2, "Null", "Null", "Null", "Null", "Null", "Null", "Null", 9, 10, 11],
         "1":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "A":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "B":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "C":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "D":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "E":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "F":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "G":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "H":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "I":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "J":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],    
         "K":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "L":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "M":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "N":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "O":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "P":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11],
         "Q":[0, 1, 2, 3, 4, 5, "Null", 6, 7, 8, 9, 10, 11]}

@ticketing.route("/ticketing", methods = ["GET", "POST"])
def Ticketing():
    msg = ""
    userdata = UserData()
    if request.method == "GET":
        if "userid" in session:
            for user in userdata:
                if user[1] == session["userid"]:
                    nowuser = user
            ticketdata = TicketData()
            return render_template("ticketing.html",
                                msg = msg,
                                place = place,
                                ticketdata = ticketdata,
                                enumerate = enumerate,
                                str = str,
                                nowuser = nowuser)
        else:
            return redirect("signin")
    elif request.method == "POST":
        ticket = request.get_json("value")
        print(ticket)
        row, column, index = ticket["value"].split()
        print(row, column, index)
        index = int(index)

        ticketdata = TicketData()
        for user in userdata:
            if user[1] == session["userid"]:
                nowuser = user
                if user[-1] == "":
                    if ticketdata[index][3] == "0":
                        with sql.connect(db_path+"/ticketdata.db") as con:
                            cur = con.cursor()
                            cur.execute(f"UPDATE ticket SET value = 1 WHERE id={index+1}")
                            con.commit()

                        with sql.connect(db_path+"/userdata.db") as con:
                            cur = con.cursor()
                            cur.execute(f"UPDATE 'userdata' SET ticket = :p WHERE name=:name", {"p": row+column+" "+str(index+1), "name":session["userid"]})
                            con.commit()

                        msg = "예매"
                    else:
                        msg = "예매된"
                else:
                    msg = "이미"

        return {"data": msg}