#!/usr/bin/python3
import sys


def convert_type(arguments):
    converted_list = []
    i = 1
    while i < len(arguments):
        converted_list.append(int(arguments[i]))
        i += 1
    return converted_list


if __name__ == "__main__":
    argv = convert_type(sys.argv)
    length = len(argv)
    result = 0
    i = 0
    while i < length:
        result += argv[i]
        i += 1
    print(result)
