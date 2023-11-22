from flask import Flask, render_template, request, redirect, session
from datetime import timedelta
from email.mime.text import MIMEText
import random
import smtplib
import sqlite3 as sql
import os
import re


app = Flask(__name__)
app.secret_key = 'NE(*F&$K#>WS:GWERGIPWR)*#HJHD?F><SDNFIYGEB^#*^G@YG(&DYFGVBYG#&^#@FUWEDF)'

C = os.path.dirname(__file__)
db_path = os.path.join(C, "database")

user_id = ""
user_password = ""
user_email = ""
msg = ""


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

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(hours=1)

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/")
def main():
    global msg
    value = ""
    userdata = UserData()
    if "userid" in session:
        for a in userdata:
            if a[1] == session["userid"]:
                value = a[-1]

    return render_template("main.html",
                           user_id = session['userid'] if "userid" in session else "",
                           msg = msg,
                           value = value)

@app.route("/newuser", methods = ["GET", "POST"])
def newuser():
    if request.method == "GET":
        return render_template("newuser.html")
    elif request.method == "POST":
        user_id = request.form.get("value")
        print(user_id)
        EMAIL = random.randrange(0, 1000000)

        session["userdata"] = [user_id, user_password, user_email, EMAIL]

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('010swan823@gmail.com', 'pxop oqce zggc zpit')
        msg = MIMEText(f'인증키 : {EMAIL}\n누구에게도 보여주지 마세요.')
        msg['Subject'] = 'TEDDYTALKCONCERT 인증'
        
        # 유효성 검사를 위한 정규표현식
        reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$" 
        if re.match(reg, user_email):
            s.sendmail('010swan823@gmail.com', user_email, msg.as_string())
            print(user_email)
            print("정상적으로 메일이 발송되었습니다.")
        else:
            print("받으실 메일 주소를 정확히 입력하십시오.")

        s.quit()

        print(EMAIL)
        # return redirect("email")
        return {"Email": EMAIL}

@app.route("/email", methods = ["GET", "POST"])
def email():
    global msg
    if request.method == "GET":
        return render_template("email.html")
    elif request.method == "POST":
        user_id = session["userdata"][0]
        user_password = session["userdata"][1]
        user_email = session["userdata"][2]
        EMAIL = session["userdata"][3]
        session.pop("userdata", None)
        try:
            email_user = request.form['email']
            print(email_user)
            if int(email_user) == EMAIL:
                print('if')
                msg = "newuser"
                with sql.connect(db_path+"/userdata.db") as con:
                    cur = con.cursor()

                    cur.execute("INSERT INTO userdata (name, email, password, ticket) VALUES (?,?,?,?)",
                                (user_id, user_email, user_password, "",))
                    con.commit()
            else:
                msg = ""
        except:
            msg = "오류발생."
        finally:
            return redirect("/")

@app.route("/logout")
def logout():
    session.pop("userid", None)
    return redirect("/")

@app.route("/login", methods = ["GET", "POST"])
def login():
    global msg
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        LogIn = False
        userdata = UserData()
        name_user = request.form["text"]
        password_user = request.form["password"]

        for data in userdata:
            if data["name"] == name_user and data["password"] == password_user:
                LogIn = True
                break
        
        if LogIn: 
            session["userid"] = name_user
            print(session)
        return redirect("/")
         
@app.route("/ticketing", methods = ["GET", "POST"])
def ticketing():
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
    msg = ""
    if request.method == "GET":
        if "userid" in session:
            ticketdata = TicketData()
            return render_template("ticketing.html",
                                   msg = msg,
                                   place = place,
                                   ticketdata = ticketdata,
                                   enumerate = enumerate,
                                   str = str)
        else:
            return redirect('login')
    elif request.method == "POST":
        ticket = request.form["data"]
        row, column, index = ticket.split()
        index = int(index)

        ticketdata = TicketData()
        userdata = UserData()
        for user in userdata:
            if user[1] == session["userid"]:
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

                        msg = "예매 하였습니다."
                    else:
                        msg = "예매된 자리입니다."
                else:
                    msg = "이미 예매하였습니다."

        return render_template("ticketing.html",
                               msg = msg)

@app.route("/userdata", methods = ["POST", "GET"])
def Userdata():
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

@app.route("/qrcode/<space>")
def qrcode(space):
    print(space)

    userdata = UserData()
    for user in userdata:
        print(user[1])
        if user[1] == session["userid"]:
            print(user[-1])
            if user[-1].split()[0] == space:
                return render_template("qrcode.html",
                                       space = space)
            else:
                return "잘못된 요청입니다."
            
    return "잘못된 요청입니다."
