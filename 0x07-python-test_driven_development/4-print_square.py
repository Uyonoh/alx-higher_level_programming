#!/usr/bin/python3

"""A module to print a square using '#'

Attributes:

"""


def print_square(size):
    """Prints a square of size 'size' using '#'

    Args:
        size (int): the size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
