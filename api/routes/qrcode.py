from flask import render_template, Blueprint, session, redirect
from .Data import UserData

QRcode = Blueprint("qrcode", __name__, template_folder="/templates")

@QRcode.route("/qrcode")
def qrcode():
    userdata = UserData()
    if "userid" in session:
        for user in userdata:
            if user[1] == session["userid"]:
                space = user[-1][0:2]
                nowuser = user
                return render_template("qrcode.html",
                                       space = space,
                                       nowuser = nowuser)
        return "잘못된 요청입니다." 
    else :
        return redirect("/")
