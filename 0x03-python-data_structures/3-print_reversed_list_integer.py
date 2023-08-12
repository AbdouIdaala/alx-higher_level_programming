#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list) - 1
    i = 0
    while length >= i:
        print("{:d}".format(i))
        length -= 1
