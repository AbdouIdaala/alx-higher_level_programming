#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1:
        print(".")
    else:
        i = 1
        while i < len(argv):
            print("{}: {}".format(i, argv[i]))
            i += 1
