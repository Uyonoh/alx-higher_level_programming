#!/usr/bin/python3

"""A module to print a users name

Attributes:

"""


def say_my_name(first_name, last_name=""):
    """Prints the first and last names of a person

    Args:
        first_name (str): the person's first name
        last_name (str, optional): the person's last name,
            defaults to an empty string

    Raises:
        TypeError: if first_name or last_name is not a string,
            or is a number in string format:'10'
        ValueError: if the first_name is an empty string

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == "":
        raise ValueError("first_name must not be an empty string")
    try:
        int(first_name)

        raise TypeError("a name must not be a number")
    except ValueError:
        pass
    try:
        int(last_name)

        raise TypeError("a name must not be a number")
    except ValueError:
        pass
    # If the names can be paserd as int it must be a number, else continue

    print("My name is {} {}".format(first_name, last_name))
