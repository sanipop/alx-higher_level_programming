#!/usr/bin/python3
"""A Scriptt."""


class Student:
    """A three method dictionary JSON."""

    def __init__(self, first_name, last_name, age):
        """The class initializer function.

        Args:
            first_name (str): the first parameter of the method.
            last_name (str): Thid id th esecond.
            age (int): Age passed ot teh class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """convert the input to JSON.

        the function is the main.

        Args:
            attrs (list): (Optional) input to conv.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """It replace the content of the dictionary.

        Args:
            json (dict): value passed fo the reload.
        """
        for k, v in json.items():
            setattr(self, k, v)
