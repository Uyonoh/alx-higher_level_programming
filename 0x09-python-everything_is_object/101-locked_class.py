#!/usr/bin/python3

"""Frozen class module
"""


class LockedClass:
    """A frozen class
    """

    def __init__(self):
        pass

    def __setattr__(self, key, value):
        """Sets the value of a attribute

        Args:
            key: the name of the attribute to be set
            value: the new value for the attribute

        Raises:
            AttributeError: if the key is not 'first_name'

        """

        if not key == "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(key))
        object.__setattr__(self, key, value)
