#!/usr/bin/python3
"""Script for printing the utf8 after reading ."""


def read_file(filename=""):
    """Print the content of utf8."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
