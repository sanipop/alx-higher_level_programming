#!/usr/bin/python3
"""
===================================
A module for inheritance
===================================
"""


def inherits_from(obj, a_class):
    """The method that is for inheritance
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
