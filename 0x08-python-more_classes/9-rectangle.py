#!/usr/bin/python3
"""the final task on basic more of class
"""


class Rectangle:
    """a rect class for compound opwrations.

    variou operations are performed on rect
     the inbuilt functions include. __str__, __repr__, and __del__
    fuctionality defined below.

    Attributes:
        number_of_instances (int): perform various operations.
        print_symbol (str): outputs to the string
            representation of rectangle

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """the initializer function of the class

        Args:
            width (int): initial value of width
            height (int): intial value of height

        """
        type(self).number_of_instances += 1
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): return value of width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): assign the value of the width

        Attributes:
            __width (int): the assign value of width

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
            __height (int): receive the value of height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): assign value to height

        Attributes:
            __height (int): value unchanged

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
        """cal the cval of area

        Attributes:
            __width (int): widht is same
            __height (int): value of the height

        Returns:
            Area of rectangle: product of adj sides

        """
        return self.__width * self.__height

    def perimeter(self):
        """sum of all sides`

        Attributes:
            __width (int): width is width
            __height (int): height is height

        Returns:
            multiply adj sides.

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """A hash representation of a rect.

        Attributes:
            __width (int): the value of width
            __height (int): height i height
            str (str): string id to be returned

        Returns:
            str (str): the output in the str format

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "{}".format(self.print_symbol)
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """function that return string.

        Returns:
            conv input to string format.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Always printable string.

        Returns:
            A string in repr format.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """Function to delete an attribute

        """
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare two seprate rect

        Args:
            rect_1 (Rectangle object): rect 1
            rect_2 (Rectangle object): and it s no 2

        Raises:
            TypeError: if `rect_1` or `rect_2` is not an instance of cls.

        Returns:
            output the rectangle with the biggest area

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Function to create square.

        Args:
            size (int): the toot of square

        Returns:
            change rectangle to square

        """
        return cls(size, size)
