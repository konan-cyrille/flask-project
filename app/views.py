from flask import render_template

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    context = {
        "username": "Cyrile"
    }
    return render_template("index.html", context=context)