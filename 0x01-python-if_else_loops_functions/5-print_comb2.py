#!/usr/bin/python3
for number in range(0, 100):
    if number != 99:
        print("{:02d}, ".format((number <= 9) + number), end='')
    else:
        print(number)
