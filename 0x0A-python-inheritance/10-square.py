#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
===================================
A module to the class square
===================================
"""


class Square(Rectangle):
    """Square that inherits from rectangle"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """the area class function"""

        return self.__size ** 2
