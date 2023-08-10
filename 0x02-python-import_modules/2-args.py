#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    length = len(argv)
    if length > 1:
        if length == 2:
            print("{} argument:".format(length - 1))
        else:
            print("{} arguments:".format(length - 1))
        i = 1
        while i < length:
            print("{}: {}".format(i, argv[i]))
            i += 1
    else:
        print("{} arguments.".format(length - 1))
