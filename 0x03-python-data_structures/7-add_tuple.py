#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_tuple_a = len(tuple_a)
    length_tuple_b = len(tuple_b)

    if length_tuple_a == 0:
        a01 = 0
        a02 = 0
    elif length_tuple_a == 1:
        a01 = tuple_a[0]
        a02 = 0
    else:
        a01 = tuple_a[0]
        a02 = tuple_a[1]

    if length_tuple_b == 0:
        b01 = 0
        b02 = 0
    elif length_tuple_b == 1:
        b01 = tuple_b[0]
        b02 = 0
    else:
        b01 = tuple_b[0]
        b02 = tuple_b[1]

    new_tuple = (a01 + b01, a02 + b02)

    return (new_tuple)
