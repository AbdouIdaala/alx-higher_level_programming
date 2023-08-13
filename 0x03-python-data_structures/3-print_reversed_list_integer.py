#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_list = []
    for item in my_list:
        new_list.insert(0, item)
    for element in new_list:
        print("{:d}".format(element))
