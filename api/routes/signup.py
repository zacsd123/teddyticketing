from flask import request, render_template, jsonify, session, redirect, Blueprint
from email.mime.text import MIMEText
import sqlite3 as sql
import random
import smtplib
import re
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

signup = Blueprint("signup", __name__, template_folder="templates")

@signup.route("/idcheck", methods = ["POST"])
def idcheck():
    if request.method == "POST":
        IsInId = False
        id = request.get_json()
        
        userdata = UserData()
        for user in userdata:
            if user[1] == id["value"]:
                IsInId = True
                break

        return jsonify({"check": IsInId})

@signup.route("/signup", methods = ["GET", "POST"])
def Signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        user = request.get_json()     
        if user["check"] == "중복체크":
            return { "static": "noncheck" }
        else:
            value = False
            user_id = user["name"]
            user_password = user["password"]
            user_email = user["email"]

            # 유효성 검사를 위한 정규표현식
            reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$" 
            if re.match(reg, user_email):
                EMAIL = random.randrange(100000, 1000000)
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login('010swan823@gmail.com', 'pxop oqce zggc zpit')
                msg = MIMEText(f'인증키 : {EMAIL}\n누구에게도 보여주지 마세요.')
                msg['Subject'] = 'TEDDYTALKCONCERT 인증'
                s.sendmail('010swan823@gmail.com', user_email, msg.as_string())
                session["userdata"] = [user_id, user_password, user_email, EMAIL]
                value = True
                s.quit()

            return { "static": value }

@signup.route("/email", methods = ["GET", "POST"])
def email():
    if request.method == "GET":
        return render_template("email.html")
    elif request.method == "POST":
        print(session)
        user_id = session["userdata"][0]
        user_password = session["userdata"][1]
        user_email = session["userdata"][2]
        EMAIL = session["userdata"][3]
        try:
            email = request.get_json()
            email_user = email["number"]

            if int(email_user) == EMAIL:
                print('if')
                with sql.connect(db_path+"/userdata.db") as con:
                    cur = con.cursor()

                    cur.execute("INSERT INTO userdata (name, email, password, ticket) VALUES (?,?,?,?)",
                                (user_id, user_email, user_password, "",))
                    con.commit()
                session.pop("userdata", None)
                msg = "성공"
            else:
                msg = "실패"
        except:
            msg = "실패"
        finally:
            return {"error": msg}
