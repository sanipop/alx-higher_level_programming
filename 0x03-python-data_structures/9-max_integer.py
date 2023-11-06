#!/usr/bin/python3

def max_integer(my_list):
    if len(my_list) == 0:
        return (None)

    current_max_num = my_list[0]
    for ind in range(len(my_list)):
        if my_list[ind] > current_max_num:
            current_max_num = my_list[ind]

    return (current_max_num)
