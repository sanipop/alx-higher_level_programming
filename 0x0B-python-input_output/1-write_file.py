#!/usr/bin/python3
"""A script for writing on a file."""


def write_file(filename="", text=""):
    """Function for writing a file.

    Args:
        filename (str): file to write to.
        text (str): The string to write.
    Returns:
        The nmumber of character.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
