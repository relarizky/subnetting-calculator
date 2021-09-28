# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : library/subnetting.py
# Copyright © Relarizky 2021


from library.subnet import Subnet


class Subnetting(Subnet):
    """
    main class for performing subnetting
    """

    def __init__(self, ip: str, netmask: str) -> None:
        self.ip = ip
        self.netmask = netmask

        Subnet.__init__(
            self,
            self.ip,
            self.netmask
        )

        self.host = 0  # host total of subnet
        self.position = 0  # subnet position
        self.network = None  # network address
        self.broadcast = None   # broadcast address
        self.host_range = {}  # host min and host max

    def calculate(self) -> None:
        """
        calculate subnetting
        """

        self._calc_hosts()
        self._calc_position()
        self._calc_network_addr()
        self._calc_broadcast_addr()
        self._find_host_range()

    def _calc_hosts(self) -> None:
        """
        calculate host total of subnet
        """

        classes = self.classes.get("class")

        if classes == "A":
            host = (self.subnet_range() * (256 ** 2)) - 2
        elif classes == "B":
            host = (self.subnet_range() * 256) - 2
        else:
            host = self.subnet_range() - 2

        self.host = host

    def _calc_position(self) -> None:
        """
        calculate subnet position
        """

        self.position = self.ip.split(".")[self.classes.get("index")]
        self.position = int(self.position) // self.subnet_range()

    def _calc_network_addr(self) -> None:
        """
        calculate network address
        """

        index = self.classes.get("index")
        network = self.ip.split(".")
        network[index] = str(self.position * self.subnet_range())

        for num in range(index + 1, 4):
            network[num] = "0"

        self.network = ".".join(network)

    def _calc_broadcast_addr(self) -> None:
        """
        calculate broadcast address
        """

        index = self.classes.get("index")
        broadcast = self.network.split(".")
        broadcast[index] = str((int(broadcast[index])+self.subnet_range())-1)

        for num in range(index + 1, 4):
            broadcast[num] = "255"

        self.broadcast = ".".join(broadcast)

    def _find_host_range(self) -> None:
        """
        find host range (min and max)
        """

        host_min = self.network.split(".")
        host_min[-1] = str(int(host_min[-1]) + 1)

        host_max = self.broadcast.split(".")
        host_max[-1] = str(int(host_max[-1]) - 1)

        self.host_range.update(
            {
                "min": ".".join(host_min),
                "max": ".".join(host_max)
            }
        )

    @property
    def output(self) -> dict:
        """
        bundle all outputs in one dictionary
        """

        return {
            "host": self.host,
            "range": self.host_range,
            "class": self.classes,
            "netmask": self.netmask,
            "position": self.position,
            "network": self.network,
            "broadcast": self.broadcast
        }
