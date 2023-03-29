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
        self.size = size

    @property
    def size(self):
        """:obj:'int'"""
        return self.__size

    @size.setter
    def size(self, value):
        if not (type(value) == int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square

        Args:

        Attributes:

        Returns:
            int: area of the square

        """

        return self.__size * self.__size

    def my_print(self):
        """prints a square using '#'

        Args:

        Attributes:

        Returns:

        """

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")

        if self.__size == 0:
            print("")
