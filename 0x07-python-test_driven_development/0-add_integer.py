#!/usr/bin/python3
# 0-add_integer.py
# Abdulmalik Sani
"""Defines an integer addition function.
   it has two variable
   it returns two integer
   the integers are a and b
"""


def add_integer(a, b=98):
    """Add integer a and b.
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
