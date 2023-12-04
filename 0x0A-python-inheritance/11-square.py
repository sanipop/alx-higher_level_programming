#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
===================================
a child class of rectangle baseclass
===================================
"""


class Square(Rectangle):
    """The main square class"""

    def __init__(self, size):
        """the initializes class"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """A Rectangle function"""

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
