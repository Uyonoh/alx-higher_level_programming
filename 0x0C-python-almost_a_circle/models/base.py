#!/urs/bin/python3

"""Base Modulu

"""


class Base:
    """A base class

    Attributes:
        __nb_objects (int): defaults to 0

    Args:
        id (int, optional): defaults to None

    """

    def __init__(self, id=None):
        __nb_objects = 0
        if not id == None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects

    @property
    def id(self):
        """:obj" 'int'"""

        return self.id

    @id.setter
    def id(self, id):
        self.id = id
