#!/usr/bin/python3
"""Script that defines rectangle."""


def add_attribute(obj, att, value):
    """function to add attributes.

    Args:
        obj (any): to add att to.
        att (str): attr to be added to.
        value (any): val of attr passed.
    Raises:
        TypeError: error if no attr passed.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
