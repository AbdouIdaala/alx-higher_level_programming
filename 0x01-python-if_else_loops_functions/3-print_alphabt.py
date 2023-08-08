#!/usr/bin/python3
for c in range(97, 123):
    if not (chr(c) == 'e' or chr(c) == 'q'):
        print("{}".format(chr(c)), end='')
