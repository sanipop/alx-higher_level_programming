#!/usr/bin/python3
"""Dclearation of the class."""


class Square:
    """Defining the class square."""

    def __init__(self, size=0):
        """Function initialising the class.

        Args:
            size (int): Integer representing the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)
