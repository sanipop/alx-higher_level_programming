#!/usr/bin/python3
"""Creating a Class."""


class Square:
    """Defining a class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Function to initialize the class.

        Args:
            size (int): A variable of name size and type int.
            position (int, int): length and breath of square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Setting the value of the variable."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Assing the corresponding value to pos."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the Area of the Square."""
        return (self.__size ** 2)

    def my_print(self):
        """Output the square of # pix."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
