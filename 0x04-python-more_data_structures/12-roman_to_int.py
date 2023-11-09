#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string or type(roman_string) != str:
        return 0
    c_T = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    To_Roman = 0

    for j in range(len(roman_string)):
        if j > 0 and c_T[roman_string[j]] > c_T[roman_string[j - 1]]:
            To_Roman += c_T[roman_string[j]] - 2 * \
                        c_T[roman_string[j - 1]]
        else:
            To_Roman += c_T[roman_string[j]]
    return To_Roman
