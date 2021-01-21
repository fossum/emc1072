

def test_bit(data, offset):
    """testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.

    Args:
        data (int): Data to modify.
        offset (int): Offset index of the bit.

    Returns:
        int: Modified data.
    """
    mask = 1 << offset
    return data & mask


def set_bit(data: int, offset: int):
    """setBit() returns an integer with the bit at 'offset' set to 1.

    Args:
        data (int): Data to modify.
        offset (int): Offset index of the bit.

    Returns:
        int: Modified data.
    """
    mask = 1 << offset
    return data | mask


def clear_bit(data: int, offset: int):
    """clearBit() returns an integer with the bit at 'offset' cleared.

    Args:
        data (int): Data to modify.
        offset (int): Offset index of the bit.

    Returns:
        int: Modified data.
    """
    mask = ~(1 << offset)
    return data & mask


def toggle_bit(data, offset):
    """toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.

    Args:
        data (int): Data to modify.
        offset (int): Offset index of the bit.

    Returns:
        int: Modified data.
    """
    mask = 1 << offset
    return data ^ mask
