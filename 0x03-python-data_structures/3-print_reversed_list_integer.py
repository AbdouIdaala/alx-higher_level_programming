#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        my_list[i] = my_list.pop(len(my_list - i - 1))
        print("{:d}".format(my_list[i]))
