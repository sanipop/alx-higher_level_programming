#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
===================================
cal area ro base geometry
===================================
"""


class Rectangle(BaseGeometry):
    """Defination of class that inherits from BAseGEometryy"""

    def __init__(self, width, height):
        """The initializeer method for attribureds"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to cal for areas"""

        return self.__width * self.__height

    def __str__(self):
        """Function to convert to string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
