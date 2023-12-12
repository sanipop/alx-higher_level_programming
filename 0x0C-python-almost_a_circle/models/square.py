#!/usr/bin/python3
"""Script for the Class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square defined."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation of the Class Square.

        Args:
            size (int): parameter size of square.
            x (int): The x cord of sqr size.
            y (int): The y cord of sqr y.
            id (int): The id of Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Setter and getter of Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Fxn to modify sqr.

        Args:
            *args (ints): Narg passed to sqr.
                - 1st argument represents id attribute
                - 2nd argument of sqr
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value passed for dictionary.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Function output the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Funct to output string."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
