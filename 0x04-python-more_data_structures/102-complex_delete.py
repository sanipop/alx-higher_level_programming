#!/usr/bin/python3
# 102-complex_delete.py
# Abdulmalik Sani  <thepersian82@gmail.com>


def complex_delete(a_dictionary, value):
    """Function to delete a dictionary."""
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
