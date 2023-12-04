#!/usr/bin/python3
"""
===================================
A more implimented basegeometry
===================================
"""


class BaseGeometry:
    """The base geometry area adv"""

    def area(self):
        """method to solve fo an area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method to check if input is an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
