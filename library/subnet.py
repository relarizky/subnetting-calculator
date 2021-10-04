# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : library/subnet.py
# Copyright © Relarizky 2021


from __future__ import annotations
from re import search as regex
from library.exception import InvalidNotation, InvalidIPAddress


class Subnet:
    """
    class for processing given subnet IP
    """

    def __init__(self, ip: str, netmask: str) -> None:

        if not self.filter_ip(ip):
            raise InvalidIPAddress(
                "your given IP address is invalid."
            )

        if not self.filter_netmask(netmask):
            raise InvalidNotation(
                "your given Netmask is invalid."
            )

        self.ip = ip
        self.netmask = netmask
        self.classes = self.subnet_class()

    @classmethod
    def with_cidr(cls, ip_with_cidr: str) -> Subnet:
        """
        create an Subnet object with CIDR prefix
        """

        ip, cidr = ip_with_cidr.split("/")

        if not cls.filter_ip(ip):
            raise InvalidIPAddress(
                "the given IP address is not valid."
            )

        if not cls.filter_cidr(int(cidr)):
            raise InvalidNotation(
                "the given CIDR prefix is not valid."
            )

        netmask = cls.cidr_to_netmask(int(cidr))

        return cls(ip, netmask)

    @staticmethod
    def filter_ip(ip: str) -> bool:
        """
        filter given IP
        """

        filter = r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}$'

        return regex(filter, ip) is not None

    @staticmethod
    def filter_cidr(cidr: int) -> bool:
        """
        filter given CIDR prefix
        """

        return (8 <= cidr <= 32)

    @staticmethod
    def filter_netmask(netmask: str) -> bool:
        """
        filter given Netmask
        """

        valid_mask = [
            0, 128, 192, 224, 240,
            248, 252, 254, 255
        ]
        filter = r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}$'

        if regex(filter, netmask) is not None:
            for mask in netmask.split("."):
                if int(mask) in valid_mask:
                    continue

                return False

            return True

        return False

    @staticmethod
    def cidr_to_netmask(cidr: int) -> str:
        """
        convert given CIDR to valid Netmask
        """

        number_1 = ["1" for total in range(cidr)]
        number_0 = ["0" for total in range(32 - cidr)]
        binary = number_1 + number_0

        binary.insert(8,  ".")
        binary.insert(17, ".")
        binary.insert(26, ".")

        binary = list(
            map(
                lambda num: str(int(num, base=2)),
                "".join(binary).split(".")
            )
        )

        return ".".join(binary)

    def subnet_range(self) -> int:
        """
        return the range of subnet
        """

        mask = list(
            filter(
                lambda num: int(num) != 255,
                self.netmask.split(".")
            )
        )

        return 255 if len(mask) == 0 else (256 - int(mask[0]))

    def subnet_class(self) -> dict:
        """
        return the class of given subnet IP
        """

        index = 0
        netmask = self.netmask.split(".")

        while (index < len(netmask)):
            if int(netmask[index]) != 255:
                break

            index += 1

        if 0 <= index <= 1:
            classes = {
                "index": 1,
                "class": "A"
            }
        elif index == 2:
            classes = {
                "index": 2,
                "class": "B"
            }
        else:
            classes = {
                "index": 3,
                "class": "C"
            }

        return classes
