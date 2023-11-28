#!/usr/bin/python3
"""A python project for calculating the peremeter of a rectanfle.
"""


class Rectangle:
    """A slass for collecting assigning and calculating teh value of the rect.

    Args:
        width (int): the integer value of the width of the rectangle
        height (int): the value assigned to be the height of the rectangle0

    """
    def __init__(self, width=0, height=0):
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): the functio serves to return the value of teh width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): the value to assigh to teh weidth

        Attributes:
            __width (int): the fun ction returns the value of the weidth

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
            __height (int): the height of the rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): value to be assigned as the length of the rectangle

        Attributes:
            __height (int): the name to be assign the value received

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """this function calulate the length of the rectangle.

        Attributes:
            __width (int): the value of the widht
            __height (int): the value passed to the height

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Function retutns the value of the sum of the sides
        Attributes:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
