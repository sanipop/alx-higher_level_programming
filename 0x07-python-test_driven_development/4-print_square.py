#!/usr/bin/python3
# 4-print_square.py
"""A function for printing hash square."""


def print_square(size):
    """a function takes size as input and prints a square.

    Args:
        size (int): varable representing length of a square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
