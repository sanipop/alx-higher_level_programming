#!/usr/bin/python3

#o function that printis an integer using tryby

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
