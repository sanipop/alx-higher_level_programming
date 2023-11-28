#!/usr/bin/python3
"""A new rectangle with delete function added.
"""


class Rectangle:
    """The normal rectangle class with delete method added.

    __str__, __repr__, and __del__ fuctionality defined below.

    Args:
        width (int): the width value of the class
        height (int): the height attribute of the class

    """
    def __init__(self, width=0, height=0):
        # the rectangle class initializer
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): horizontal dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): the value passed to the widrh

        Attributes:
            __width (int): the function to set the value of the weidth

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
            __height (int): return the height of the function

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): the value passed to set the height

        Attributes:
            __height (int): the height  assigned

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
        """Product of the sides of the rectangle`.

        Attributes:
            __width (int): the width peremetr of the rectanglr
            __height (int): the height parameter of the area

        Returns:
            Area of rectangle: the product of the two sides

        """
        return self.__width * self.__height

    def perimeter(self):
        """Add all the sides of the rectangle

        Attributes:
            __width (int): the lower size of the rectangle
            __height (int): the othe r adjacent side of the rctangle

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """the hash representation of the rectangle

        Attributes:
            __width (int): the weidth of the rectanglr
            __height (int): vthe height of the rectangle is represented witght
            str (str): string to constructed for return

        Returns:
            str (str): sfunction to format the sting

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """for formating the area or peremeter for printing.

        Returns:
            The output of _draw_rectangle, which creates a string
        representation of the rectangle suitable for printing.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval().

        Returns:
            the repr method of the formatting.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def __del__():
        """the function that delete the variable.

        """
        print('Bye rectangle...')
