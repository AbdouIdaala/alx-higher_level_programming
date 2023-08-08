#!/usr/bin/python3
for number in range(0, 100):
    if number != 99:
        print("{:02d}, ".format((number < 99) + number - 1), end='')
    else:
        print(number)
