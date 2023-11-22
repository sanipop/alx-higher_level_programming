#!/usr/bin/python3
"""Creating the Class."""


class Square:
    """A Class of Square."""

    def __init__(self, size=0):
        """Initializer of the classe.

        Args:
            size (int): a variable of the namee size.
        """
        self.size = size

    @property
    def size(self):
        """Function to initialize size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """function to calculate the area of a square."""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Function to compare 2 area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Function to vheck not equality."""
        return self.area() != other.area()

    def __lt__(self, other):
        """function to check less than."""
        return self.area() < other.area()

    def __le__(self, other):
        """Function to check if less than or equal to."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Function ot check if grater than."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Function to check if grater than or equal to."""
        return self.area() >= other.area()
