#!/usr/bin/python3
"""Script for dictionary to jSON"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """the initializers.

        Args:
            first_name (str): The first parameter passed.
            last_name (str): Surname for the class.
            age (int): integer passed of the age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Json rep ofdict."""
        return self.__dict__
