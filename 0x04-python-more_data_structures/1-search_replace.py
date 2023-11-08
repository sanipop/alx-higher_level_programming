#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return
    mod_list = my_list[:]
    for cell, val in enumerate(mod_list):
        if val == search:
            mod_list[cell] = replace
    return mod_list
