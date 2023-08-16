#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        big_num = 0
        for value in a_dictionary.values():
            if value > big_num:
                big_num = value
        for key in a_dictionary.keys():
            if a_dictionary.get(key) == big_num:
                return key
