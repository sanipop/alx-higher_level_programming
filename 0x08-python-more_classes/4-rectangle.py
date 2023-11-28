#!/usr/bin/python3
"""The task 4 for the Rectangle project.
"""


class Rectangle:
    """A special function for calculating various attribute of a rectangle.

    __str__ and __repr__ fuctionality defined below.

    Args:
        width (int): the weidth attribute of the rectangle
        height (int): the height passed fo the class

    """
    def __init__(self, width=0, height=0):
        # the initializer for the various attribute of rectangle
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
            value (int): the value assigned to the weidth

        Attributes:
            __width (int): the function function to pass weidth to value

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
            __height (int): the function for returning the value of the height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): the value passed to the height

        Attributes:
            __height (int): the variable to pass the heigt to

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
        """calculate  the product of the sides.

        Attributes:
            __width (int): the value passed to the weidth
            __height (int): the height of the rectangle

        Returns:
            Area of rectangle: return the product ot the adjacent sides

        """
        return self.__width * self.__height

    def perimeter(self):
        """return the value of the peremeter

        Attributes:
            __width (int): the weiddth attribute of the peremetrer
            __height (int): the height value of the peremeter

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Display the # representation of the rectangle.

        Attributes:
            __width (int): the value of the width of the # repreentation
            __height (int): the value of the height # representation
            str (str): string to constructed for return

        Returns:
            str (str): Convert the # diagram to to a string suitable for diy

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """the string representation of the rect convert method.

        Returns:
            string formatter of the of the rectanglr.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """a function for its reoresentation.

        Returns:
            the value that can be erepresented .

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
