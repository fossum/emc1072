"""Module interfacing with the EMC1072 status register."""


class StatusStruct(int):
    """Represents data held in the EMC1072 status register."""

    INT_LIMIT_OFFSET = 0
    EXT_LIMIT_OFFSET = 1
    FAULT_OFFSET = 2
    EXT_LOW_OFFSET = 3
    EXT_HIGH_OFFSET = 4
    INT_LOW_OFFSET = 5
    INT_HIGH_OFFSET = 6
    BUSY_OFFSET = 7

    def __init__(self, register):
        self._register = register

    def __repr__(self):
        """Printable representation of Status."""
        return repr(f"<status.Status; busy: {self.busy}, fault: {self.fault}, i-low: {self.internal_low}, i-high: {self.internal_high}, i-limit: {self.internal_limit}>")

    @property
    def internal_limit(self):
        return bool(self._register & (1 << self.INT_LIMIT_OFFSET))

    @property
    def external_limit(self) -> bool:
        """Returns bool representing external_limit."""
        return bool(self._register & (1 << self.EXT_LIMIT_OFFSET))

    @property
    def fault(self) -> bool:
        """Returns bool representing fault."""
        return bool(self._register & (1 << self.FAULT_OFFSET))

    @property
    def external_low(self) -> bool:
        """Returns bool representing external_low."""
        return bool(self._register & (1 << self.EXT_LOW_OFFSET))

    @property
    def external_high(self) -> bool:
        """Returns bool representing external_high."""
        return bool(self._register & (1 << self.EXT_HIGH_OFFSET))

    @property
    def internal_low(self) -> bool:
        """Returns bool representing internal_low."""
        return bool(self._register & (1 << self.INT_LOW_OFFSET))

    @property
    def internal_high(self) -> bool:
        """Returns bool representing internal_high."""
        return bool(self._register & (1 << self.INT_HIGH_OFFSET))

    @property
    def busy(self) -> bool:
        """Returns bool representing busy."""
        return bool(self._register & (1 << self.BUSY_OFFSET))

class Status():
    """Interface to the status register."""

    REGISTER_ADDRESS = 0x02

    def __init__(self, bus, chip_address):
        self._bus = bus
        self._chip_address = chip_address

    def __call__(self) -> StatusStruct:
        return StatusStruct(self._bus.read_byte_data(self._chip_address, Status.REGISTER_ADDRESS))
