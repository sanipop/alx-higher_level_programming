#!/usr/bin/python3
"""The script ofr 10 task."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the class of a square."""

    def __init__(self, size):
        """the initializer method.

        Args:
            size (int): passing a size integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
