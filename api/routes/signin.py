from flask import Blueprint, redirect, session, request, render_template
from .Data import UserData, C

signin = Blueprint("signin", __name__, template_folder="templates")

@signin.route("/signin", methods = ["GET", "POST"])
def Signin():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        user = request.get_json()
        LogIn = False
        userdata = UserData()
        id = user["id"]
        password = user["password"]

        for data in userdata:
            if data["name"] == id and data["password"] == password:
                LogIn = True
                break
        
        if LogIn: 
            session["userid"] = id
            print(session)
        return {"value": LogIn}
    

@signin.route("/logout")
def logout():
    session.pop("userid", None)
    return redirect("/")
