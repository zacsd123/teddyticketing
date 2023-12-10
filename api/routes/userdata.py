from flask import Blueprint, redirect, request, session, render_template
import sqlite3 as sql
import os

C = os.getcwd()
db_path = os.path.join(C, "database")

def UserData():
    with sql.connect(db_path+"/userdata.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from userdata")
        userdata = cur.fetchall()
    return userdata

users = Blueprint("userdata", __name__, template_folder="templates")

@users.route("/userdata", methods = ["POST", "GET"])
def Userdata():
    if "userid" in session:
        userdata = UserData()
        for user in userdata:
            if user[1] == session["userid"]:
                nowuser = user
        if request.method == "GET":
            return render_template("userdata.html",
                                nowuser = nowuser)
        elif request.method == "POST":
            uaerticket, index = request.form["uaerticket"].split()
            index = int(index)
            with sql.connect(db_path+"/ticketdata.db") as con:
                cur = con.cursor()
                cur.execute(f"UPDATE ticket SET value = 0 WHERE id={index}")
                con.commit()
            with sql.connect(db_path+"/userdata.db") as con:
                cur = con.cursor()
                cur.execute(f"UPDATE 'userdata' SET ticket = :p WHERE name=:name", {"p": "", "name":session["userid"]})
                con.commit()
            return redirect("userdata")
    else:
        return redirect("/signin")
