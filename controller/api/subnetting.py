# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/api/subnetting.py
# Copyright © Relarizky 2021


from re import search as regex
from flask import request
from flask_restx import Resource
from library.subnetting import Subnetting
from app import api_object as api


@api.route("/")
class SubnettingAPI(Resource):
    """
    API for performing Subnetting
    """

    def get(self):
        """
        represents GET method
        """

        return {"message": "Hello World!"}

    def post(self):
        """
        represents POST method
        """

        if request.json is None:
            return {"status": False, "message": "please, input required field."}

        ip_address = request.json.get("ip")
        subnet_mask = request.json.get("netmask")

        if regex(r'/[\d]+$', ip_address) is not None:
            try:
                subnetting = Subnetting.with_cidr(ip_address)
                subnetting.calculate()
            except Exception as error_message:
                return {"status": False, "message": str(error_message)}
        else:
            try:
                subnetting = Subnetting(ip_address, subnet_mask)
                subnetting.calculate()
            except Exception as error_message:
                return {"status": False, "message": str(error_message)}

        return {"status": True, "output": subnetting.output}
