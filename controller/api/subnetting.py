# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/api/subnetting.py
# Copyright © Relarizky 2021


from re import search as regex
from flask import request
from flask_restx import Resource, fields
from library.subnetting import Subnetting
from app import api_object as api


valid_field = api.model(
    'Subnetting', {
        "ip": fields.String(
            example="192.168.100.243",
            description="192.168.100.0/25 or 192.168.100.0"
        ),
        "netmask": fields.String(
            example="255.255.255.128",
            description="255.255.255.0"
        )
    }
)


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

    @api.expect(valid_field)
    @api.doc(responses={
        200: "Success",
        400: "Required field is not provided or invalid",

    })
    def post(self):
        """
        represents POST method
        """

        if request.json is None:
            return {
                "status": False,
                "message": "please, input required field."
            }, 400

        ip_address = request.json.get("ip") or ""
        subnet_mask = request.json.get("netmask") or ""

        if regex(r'/[\d]+$', ip_address) is not None:
            try:
                subnetting = Subnetting.with_cidr(ip_address)
                subnetting.calculate()
            except Exception as error_message:
                return {"status": False, "message": str(error_message)}, 400
        else:
            try:
                subnetting = Subnetting(ip_address, subnet_mask)
                subnetting.calculate()
            except Exception as error_message:
                return {"status": False, "message": str(error_message)}, 400

        return {"status": True, "output": subnetting.output}, 200
