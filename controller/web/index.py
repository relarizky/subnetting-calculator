# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/web/index.py
# Copyright © Relarizky 2021


from flask import render_template
from app import app_object as app


@app.route("/")
@app.route("/index")
def index():
    """
    represents index / home page
    """

    return render_template("index.html")
