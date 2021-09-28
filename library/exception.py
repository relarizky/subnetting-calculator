# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : library/exception.py
# Copyright © Relarizky 2021


class InvalidNotation(Exception):
    """
    raised when user input invalid notation (CIDR / Netmask)
    """

    def __init__(self, message: str) -> None:

        self.message = message

        Exception.__init__(self, message)


class InvalidIPAddress(Exception):
    """
    raised when user input invalid IP Address
    """

    def __init__(self, message: str) -> None:

        self.message = message

        Exception.__init__(self, message)
