#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
===================================
A python class for rectangle area
===================================
"""


class Rectangle(BaseGeometry):
   """Recatngle inherits from baseGeometry and cal area
   """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
