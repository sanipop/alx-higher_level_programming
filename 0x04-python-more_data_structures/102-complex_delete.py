#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for ndex in list(a_dictionary):
        if a_dictionary[ndex] == value:
            del a_dictionary[ndex]
    return a_dictionary
