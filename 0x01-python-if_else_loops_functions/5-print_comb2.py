#!/usr/bin/python3
for number in range(0, 100):
    if number != 99 and number < 10:
        print("{:02}, ".format(number), end='')
    elif number != 99 and number >= 10:
        print("{}, ".format(number), end='')
