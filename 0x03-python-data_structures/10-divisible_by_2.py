#!/usr/bin/python3

def divisible_by_2(my_list=[]):

   even = []
    for ind in range(len(my_list)):
        if my_list[ind] % 2 == 0:
            even.append(True)
        else:
            even.append(False)

    return (even)
