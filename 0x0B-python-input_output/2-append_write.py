#!/usr/bin/python3
"""Script for appending file"""


def append_write(filename="", text=""):
    """Function for adding to a text flie.

    Args:
        filename (str): The name of fie to write to.
        text (str): string to write to.
    Returns:
        count of the character written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
