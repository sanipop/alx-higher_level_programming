#!/usr/bin/python3

"""
 a function that prints the first unknown elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    outp = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            outp += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (outp)
