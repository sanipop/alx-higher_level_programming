#!/usr/bin/python3

def no_c(my_string):
    rep = ''
    for alp in my_string:
        if alp != 'c' and alp != 'C':
            rep += alp
            return (rep)
