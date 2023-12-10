from flask import Blueprint, session, render_template, redirect

main = Blueprint("main", __name__, template_folder="/templates")

@main.route("/")
def Main():
    if "userid" in session:
        return redirect("/userdata")

    return render_template("main.html",
                           user_id = session['userid'] if "userid" in session else "")