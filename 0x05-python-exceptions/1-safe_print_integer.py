#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value/0))
    except (TypeError, ZeroDivisionError):
        return False
    else:
        return True
