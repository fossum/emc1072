"""Module for the EMC1072 temperature sensor."""

from smbus2 import SMBus

from .configuration import Configuration
from .status import Status
from .temp import Temperature


class EMC1072():
    """Interface to the EMC1072 temperature sensor."""

    def __init__(self, bus: int, chip_address: int=0x4c):
        self._bus = SMBus(bus)
        self._chip_address = chip_address

        self.status = Status(self._bus, self._chip_address)
        self.configuration = Configuration(self._bus, self._chip_address)
        self.temperature = Temperature(self._bus, self._chip_address)

    def __del__(self):
        self._bus.close()
