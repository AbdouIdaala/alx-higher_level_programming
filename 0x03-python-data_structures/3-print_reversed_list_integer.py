#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_list = [my_list[i] for i in range(len(my_list)-1, -1, -1)]

    for element in new_list:
        print("{:d}".format(element))
