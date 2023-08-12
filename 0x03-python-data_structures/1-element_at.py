#!/usr/bin/python3

def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return None
    i = 0
    while i < length:
        if i == idx:
            return my_list[i]
        i += 1
