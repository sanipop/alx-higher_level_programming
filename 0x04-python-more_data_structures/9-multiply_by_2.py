#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Multiply each value in the given dictionary by 2 and return a new dictionary.

    Parameters:
    - a_dictionary (dict): The input dictionary.

    Returns:
    - dict: A new dictionary where each value is multiplied by 2.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
