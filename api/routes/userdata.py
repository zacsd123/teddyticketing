from flask import Blueprint, redirect, request, session, render_template
import sqlite3 as sql
from Data import UserData, db_path

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