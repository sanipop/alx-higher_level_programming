#!/usr/bin/python3
"""
===========================
Module to create class mylist
===========================
"""


class MyList(list):
    """The class that does  the printing"""
    pass

    def print_sorted(self):
        """A method for printing sorted listt"""

        print(sorted(list(self)))
