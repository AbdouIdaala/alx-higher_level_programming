#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, int):
        print(str(number)[-1], end='')
        return str(number)[-1]
