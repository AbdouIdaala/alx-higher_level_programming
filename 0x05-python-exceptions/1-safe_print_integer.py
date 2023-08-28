#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value+0))
    except (TypeError, ValueError):
        return False
    else:
        return True
