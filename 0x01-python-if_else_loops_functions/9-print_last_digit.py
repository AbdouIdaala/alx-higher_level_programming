#!/usr/bin/python3
def print_last_digit(number):
    print(str(number)[-1], end='')
    return str(number)[-1]


n = print_last_digit(98)
print(n)
n = print_last_digit(-98)
print(n)
n = print_last_digit(00)
print(n)
n = print_last_digit("Holberton")
print(n)
