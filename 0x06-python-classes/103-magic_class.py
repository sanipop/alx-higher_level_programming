#!/usr/bin/python3
"""Code to calculate MagicByte."""

import math


class MagicClass:
    """MagicClass Class Defination."""

    def __init__(self, radius=0):
        """Initializing the value of the class.

        Arg:
            radius (float or int): The value passed as radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of the magic class."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate the Circumfrence of the cycle."""
        return (2 * math.pi * self.__radius)
