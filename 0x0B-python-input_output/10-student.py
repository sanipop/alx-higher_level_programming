#!/usr/bin/python3
"""String that retrives dict rep"""


class Student:
    """student class that retrives dict rep of stnt."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the first variavle passed to the class.
            last_name (str): The last variable passed to the class.
            age (int): The age of the class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """convert the dictoionary to json.

        It is the 10 student project.

        Args:
            attrs (list): (Optional) the function input.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
