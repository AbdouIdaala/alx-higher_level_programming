#!/usr/bin/python3
for c in range(90, 64, -1):
    print("{}".format(chr(c + ((c % 2) == 0) * 32)), end='')
