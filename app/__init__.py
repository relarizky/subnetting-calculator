# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : app/__init__.py
# Copyright © Relarizky 2021


from flask import Flask
from flask_restx import Api
from random import randint


app_object = Flask(
    __name__,
    static_folder="../asset",
    template_folder="../view"
)
app_object.config.update({"DEBUG": True})
app_object.config.update({"SECRET_KEY": str(randint(10000, 31337))})
api_object = Api(app_object, prefix="/api", doc="/api/doc")


import app.filter
import controller.web.index
import controller.api.subnetting
