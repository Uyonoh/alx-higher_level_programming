#!/usr/bin/python3

"""A module with a square class

Attributes:
"""


class Square:
    """A class that defines a square

    Args:
        size (int): the size of the square

    Attributes:
        __size: private size of square

    """

    def __init__(self, size=0):
        self._size = size

    @property
    def _size(self):
        """:obj:'int'"""
        return self.__size

    @_size.setter
    def _size(self, size):
        if not (type(size) == int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
