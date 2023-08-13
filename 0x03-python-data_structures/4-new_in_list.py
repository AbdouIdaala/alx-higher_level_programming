#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = []
    if idx < 0 or idx >= length:
        for ele in my_list:
            new_list.append(ele)
        return new_list
    i = 0
    while i < length:
        if i != idx:
            new_list.append(my_list[i])
        else:
            new_list.append(element)
        i += 1
    return new_list
