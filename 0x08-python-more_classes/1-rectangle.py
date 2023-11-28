#!/usr/bin/python3
"""The rectangler class with width and height.
"""


class Rectangle:
    """This is the defination of the class.

    Args:
        width (int): the span of the rectangle
        height (int): the height of the rectangle

    """
    def __init__(self, width=0, height=0):
        # This is the basic initializer of the values
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): the value of the rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): The value pased to the with function

        Attributes:
            __width (int): the value passed to the width function

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): The value of th height passed to the function

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): pass the value of height to its content

        Attributes:
            __height (int): the setter function of the height

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
