#!/usr/bin/python3

def uniq_add(my_list=None):
    """
    Add unique elements of the given list and return the sum.

    Parameters:
    - my_list (list or None): The input list. Defaults to an empty list if None.

    Returns:
    - int: The sum of unique elements in the list.
    """
    return sum(set(my_list)) if my_list else 0
