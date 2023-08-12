#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_list
    i = 0
    while i < length:
        if i == idx:
            my_list[i] = element
        i += 1
    return my_list
