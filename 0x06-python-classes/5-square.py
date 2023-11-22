#!/usr/bin/python3
"""Defination of the class ."""


class Square:
    """Creation of a class called Square."""

    def __init__(self, size):
        """A function that initialize the class.

        Args:
            size (int): the size var of type int.
        """
        self.size = size

    @property
    def size(self):
        """Function to assign the the size variable."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function to calculate the area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Using the # to print square."""
        for a in range(0, self.__size):
            [print("#", end="") for b in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
