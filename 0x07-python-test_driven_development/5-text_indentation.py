#!/usr/bin/python3

"""A module to print a text with special formatting

Attributes:

"""


def text_indentation(text):
    """Prints a text wit 2 new lines after '.', '?' and ':'

    Args:
        text (str): a string of text

    Raises:
        TypeError: if text is not a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    text = text.replace(". ", "\n\n")
    text = text.replace("? ", "\n\n")
    text = text.replace(": ", "\n\n")

    text = text.replace(".", "\n\n")
    text = text.replace("?", "\n\n")
    text = text.replace(":", "\n\n")

    print(text, end="")
