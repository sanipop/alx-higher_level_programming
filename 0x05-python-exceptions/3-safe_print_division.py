#!/usr/bin/python3
#try by function for division

def safe_print_division(a, b):
    rez = None
    try:
        rez = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(rez))
        return rez
