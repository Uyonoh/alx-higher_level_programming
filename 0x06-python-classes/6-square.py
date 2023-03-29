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

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """:obj:'tuple'"""

        return self.__position

    @position.setter
    def position(self, value):
        self.is_2tuple = (isinstance(value, tuple)) and (len(value) == 2)
        self.int_vals = isinstance(value[0], int) and isinstance(value[1], int)
        if self.int_vals:
            self.pos_int = (value[0] >= 0) and (value[1] >= 0)

        if not (self.is_2tuple and self.int_vals and self.pos_int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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

        for i in range(self.position[1]):
            print("")

        for i in range(self.__size):
            for i in range(self.position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

        if self.__size == 0:
            print("")
