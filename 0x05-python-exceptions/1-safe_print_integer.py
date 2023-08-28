#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if (value != True) and (value != False):
            print("{:d}".format(value+0))
    except TypeError:
        return False
    else:
        return True
