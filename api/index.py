from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/about')
def about():
    return 'About'
