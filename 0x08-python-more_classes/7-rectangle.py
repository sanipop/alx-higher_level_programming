#!/usr/bin/python3
"""the fuction for calculating rectangle.
"""


class Rectangle:
    """Special class of the Rectangle.

    works with height ang weidth aprameter
    it eorks with function. __str__, __repr__, and __del__
    fuctionality defined below.

    Attributes:
        number_of_instances (int): count the calls to the class.
        print_symbol (str): a string char representation of rectangle

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializer of the function class

        Args:
            width (int): width of ttha rectangle
            height (int): height of the rectangle

        """
        type(self).number_of_instances += 1
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): the weidth of the rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): value passed to the rect.

        Attributes:
            __width (int): horizontal dimension of rectangle

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
            __height (int): vertical dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): height set rect

        Attributes:
            __height (int): vertical dimension of rectangle

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
        """calculate the area

        Attributes:
            __width (int): the widht of the weidth
            __height (int): heigth of the rect

        Returns:
            Area of rectangle: profuct of adj sides

        """
        return self.__width * self.__height

    def perimeter(self):
        """cal the peremeter

        Attributes:
            __width (int): widht of the rect
            __height (int): height of the rect

        Returns:
            output the peremeter

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """the hash map of the rect.

        Attributes:
            __width (int): weidth of the rect
            __height (int): height of the rect
            str (str): string to constructed for return

        Returns:
            str (str): hash output

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "{}".format(self.print_symbol)
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """formating string to str.

        Returns:
            output the str.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """representation output string.

        Returns:
            output repesentational string.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """deletion of instance.

        """
        cls.number_of_instances -= 1
        print('Bye rectangle...')
