#!/usr/bin/python3
"""the task 6 of the rectangle calss.
"""


class Rectangle:
    """And advancced implementation of rectangle.

    Tits input include height and weight
    usees these methods __str__, __repr__, and __del__
    fuctionality defined below.

    Attributes:
        number_of_instances (int): the counter for class call

    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializer of the function

        Args:
            width (int): the weidth of the rectangle
            height (int): the height attribute os the rectangle

        """
        type(self).number_of_instances += 1
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): same value of weidth

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): value of weidth passed

        Attributes:
            __width (int): the value passed of weidth

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
            __height (int): return the height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): the height of the rectangle

        Attributes:
            __height (int): Heigh tof the rectangle

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
        """Returns area of a rectangle

        Attributes:
            __width (int): the height papendicular
            __height (int): the height of the rectange

        Returns:
            Area of rectangle: __width * __height

        """
        return product of adj side

    def perimeter(self):
        """Returns the parametrer of the rectangle

        Attributes:
            __width (int): the input weidth
            __height (int): same as the height

        Returns:
            mathematical value calculation

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """The hash representation of the rectangle.

        Attributes:
            __width (int): the same as weidth
            __height (int): the same rectangle
            str (str): string to constructed for return

        Returns:
            str (str): sout put the hash representation

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """structure for printing.

        Returns:
            it convert the various format to printable.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """a representainon format.

        Returns:
            string representation format.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """Function to delete the elemaents.

        """
        cls.number_of_instances -= 1
        print('Bye rectangle...')
