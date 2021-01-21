""""""

from smbus2 import SMBus

from . import bit_util


class ConfigurationStruct(int):
    """Represents data held in the status register."""
    DAVG_DIS_OFFSET = 1
    RANGE_OFFSET = 2
    ALERT_COMP_OFFSET = 5
    RUN_STOP_OFFSET = 6
    MASK_ALL_OFFSET = 7

    def __init__(self, data):
        self._data = data

    @property
    def davg_dis(self):
        return bool(self._data & (1 << self.DAVG_DIS_OFFSET))

    @property
    def range(self):
        return bool(self._data & (1 << self.RANGE))

    @property
    def alert_comp(self):
        return bool(self._data & (1 << self.ALERT_COMP_OFFSET))

    @property
    def run_stop(self):
        return bool(self._data & (1 << self.RUN_STOP_OFFSET))

    @property
    def mask_all(self):
        return bool(self._data & (1 << self.MASK_ALL_OFFSET))


class Configuration():

    REGISTER_ADDRESS = 0x03

    def __init__(self, bus, chip_address):
        self._bus = bus
        self._chip_address = chip_address

    @property
    def register(self):
        data = None
        with SMBus(self._bus) as bus:
            data = bus.read_byte_data(self._chip_address, self.REGISTER_ADDRESS)
        return ConfigurationStruct(data)

    @property
    def range(self):
        return self.register.range

    @range.setter
    def range(self, value):
        register = self.register
        function = set_bit
        if value:
            register = set_bit(register, ConfigurationStruct.RANGE_OFFSET)
        else:
            register = clear_bit(register, Configuration.RANGE_OFFSET)
        with SMBus(self._bus) as bus:
            data = bus.write_byte_data(self._chip_address, self.REGISTER_ADDRESS, register)
        return register
