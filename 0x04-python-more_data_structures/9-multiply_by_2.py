#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dic = {}
    for index in a_dictionary:
        mul_dic[index] = a_dictionary[index] * 2
    return mul_dic
