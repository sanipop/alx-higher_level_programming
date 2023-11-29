#!/usr/bin/python3
# 3-say_my_name.py
"""A fuction that print name to stdin."""


def say_my_name(first_name, last_name=""):
    """The function to print name.

    Args:
        first_name (str): The first string input.
        last_name (str): The second string input.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
