#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    new_list = []
    for i in range(length, 0, -1):
        new_list.append(my_list[i])
    for i in new_list:
        print("{:d}".format(i))
