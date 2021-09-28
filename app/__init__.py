# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : app/__init__.py
# Copyright © Relarizky 2021


from flask import Flask
from flask_restplus import Api
from random import randint


app_object = Flask(__name__, static_folder="../asset")
app_object.config.update({"DEBUG": True})
app_object.config.update({"SECRET_KEY": randint(10000, 31337)})
api_object = Api(app_object, prefix="/calculator")


import app.filter
import app.register
