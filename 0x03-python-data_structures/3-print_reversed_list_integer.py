#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        last = my_list.pop()
        print("{:d}".format(last))
