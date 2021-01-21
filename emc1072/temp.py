
class Temperature():
    def __init__(self, bus, chip_address):
        self._bus = bus
        self._chip_address = chip_address

    @property
    def internal_temperature(self) -> float:
        """Returns internal temperature in celsius."""
        HIGH_BYTE_ADDRESS = 0x00
        LOW_BYTE_ADDRESS = 0x29

        temp = float(self._bus.read_byte_data(self._chip_address, HIGH_BYTE_ADDRESS))
        low = self._bus.read_byte_data(self._chip_address, LOW_BYTE_ADDRESS)

        if low & (1 << 5):
            temp += 0.125
        if low & (1 << 6):
            temp += 0.25
        if low & (1 << 7):
            temp += 0.5

        return temp

    @static_method
    def c_to_f(c: float) -> float:
        """Convert celsius temperature to fahrenheit.

        Args:
            c (float): Temperature in celsius.

        Returns:
            float: Temperature in fahrenheit.
        """
        return (c * 1.8) + 32
