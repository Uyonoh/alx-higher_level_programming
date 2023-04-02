#!/usr/bin/python3

"""A module to add two numbers

Args:

Attributes:
"""


def add_integer(a: str, b=98):
    """A function to add two numbers

    Args:
        a (int or float): First number
        b (int or float, optional): Second number. Defaults to 98

    Returns:
        int: sum of a and b

    Raises:
        TypeError: If a or b is not a integer or float
    """

    isintf_a = isinstance(a, int) or isinstance(a, float)
    isintf_b = isinstance(b, int) or isinstance(b, float)

    if not isintf_a:
        raise TypeError("a must be an integer")

    if not isintf_b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
