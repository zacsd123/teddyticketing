from flask import Flask, session
from datetime import timedelta
import sqlite3 as sql
from .routes import main, signin, signup, ticketing, userdata, qrcode

app = Flask(__name__)
app.register_blueprint(main.main)
app.register_blueprint(signin.signin)
app.register_blueprint(signup.signup)
app.register_blueprint(ticketing.ticketing)
app.register_blueprint(userdata.users)
app.register_blueprint(qrcode.QRcode)
app.secret_key = "NE(*F&$K#>WS:GWERGIPWR)*#HJHD?F><SDNFIYGEB^#*^G@YG(&DYFGVBYG#&^#@FUWEDF)"

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(hours=1)
         

if __name__ == "__main__":
    app.run(debug=True)
