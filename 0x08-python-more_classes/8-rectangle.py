#!/usr/bin/python3
"""the 8th iteration of the class.
"""


class Rectangle:
    """customised rect calculator
    methods created are. __str__, __repr__, and __del__.

    Attributes:
        number_of_instances (int): increament counter for every call.
        print_symbol (str): output the representation

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """the class initialiser

        Args:
            width (int): the value of weidth
            height (int): the value of height

        """
        type(self).number_of_instances += 1
        # attribute assigment here engages setters defined below
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
            value (int): assign value to width

        Attributes:
            __width (int): the value of the rect weidth

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
            __height (int): grt the height of the rect

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): height of the rect

        Attributes:
            __height (int): height of the rectangle

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
        """product of the adjacent sides.

        Attributes:
            __width (int): the value of the weidth
            __height (int): height is height

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """sun of all the sides

        Attributes:
            __width (int): width is width
            __height (int): height is height

        Returns:
            sum all sides and return

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """hash representation of the square.

        Attributes:
            __width (int): the val of weidth
            __height (int): the val of heighth
            str (str): string is the required output format

        Returns:
            str (str): sthe value should be in strings

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "{}".format(self.print_symbol)
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """conv to str format

        Returns:
            A rect of str.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """A repr format.

        Returns:
            A string rpr format.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """function for deletion

        """
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compaere 2 diffrent rect.

        Args:
            rect_1 (Rectangle object): frect 1 to be compared
            rect_2 (Rectangle object): rect2 2 to be compared

        Raises:
            TypeError: if `rect_1` or `rect_2` is not an instance of cls.

        Returns:
            he rect with the larger size

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
