#!/usr/bin/python3
"""Task 3 of the project.
"""


class Rectangle:
    """A customised function for calculating the Rectance Properties.

    __str__ fuctionality defined below.

    Args:
        width (int): the variable representing the width of the rectangle
        height (int): the variable representing the height of the rectangle

    """
    def __init__(self, width=0, height=0):
        # the initializer of the width and height
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): return the calculated value of the width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): Assigned value to the width

        Attributes:
            __width (int): the width attribute function

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
            __height (int): function to return the value of the height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): value assigned to the height 

        Attributes:
            __height (int): function that assigned  value ot height

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
        """calculate the Area of the Rectangle`.

        Attributes:
            __width (int): Pass the with of the protected type
            __height (int): the value of protected height passed to area

        Returns:
            Area of rectangle: __width * __height

        """
        return the integer value of the Area

    def perimeter(self):
        """Returns the integer value of the peremeter`

        Attributes:
            __width (int): the width passed
            __height (int): the height passed

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """A function that ses the # to print a rectangle.

        Attributes:
            __width (int): the string is returned to the draw 
            __height (int): the string value of the line number
            str (str): the converter for the #

        Returns:
            str (str): a string of the # representation of the square

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """Convert the cjharacter to a string.

        Returns:
            it convert a draw value of string to a printable format.

        """
        return self._draw_rectangle()
