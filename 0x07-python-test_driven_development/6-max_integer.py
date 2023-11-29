#!/usr/bin/python3
"""This python script calculate for max number
"""


def max_integer(list=[]):
    """it takes inputs, and retutn the max number
        with return val of none when empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
