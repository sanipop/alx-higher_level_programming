#!/usr/bin/python3
"""A Base GEometry calss that inherits from Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class Rectangle."""

    def __init__(self, width, height):
        """The initializer of Rectangle.

        Args:
            width (int): width of the class.
            height (int): height of the class.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """cal the area of the class."""
        return self.__width * self.__height

    def __str__(self):
        """conv print() and str()  of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
