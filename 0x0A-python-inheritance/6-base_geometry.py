#!/usr/bin/python3
"""
===================================
The clas with BAse geometry
===================================
"""


class BaseGeometry:
    """the base geometry that cal area"""

    @classmethod
    def area(self):
        """method for calculated area"""

        raise Exception("area() is not implemented")
