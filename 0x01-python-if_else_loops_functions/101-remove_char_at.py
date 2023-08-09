#!/usr/bin/python3
"""
Write a function that creates a copy of the string
removing the character at the position n (not the Python way, the “C array index”).
"""


def remove_char_at(str, n):
    copy = ""
    i = 0
    while i < len(str):
        if i != n:
            copy += str[i]
        i += 1
    return copy


print(remove_char_at("Best School", 3))
