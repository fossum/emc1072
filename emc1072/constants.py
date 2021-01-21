
from enum import IntEnum


class REGISTER(IntEnum):
    INT_DATA_HIGH_BYTE = 0
    EXT_DATA_HIGH_BYTE = 1
    STATUS = 2
    CONFIG = 3
    CONV_RATE = 4
    INT_HIGH_LIMIT = 5
    INT_LOW_LIMIT = 6
    EXT_HIGH_LIMIT = 7
    EXT_LOW_LIMIT = 8
    CONFIG2 = 9
    CONV_RATE2 = 10
