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


"""
The output should be:
    Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
    : (or . if no arguments were passed) followed by a new line, followed by (if at least one argument),
    one line per argument:
    the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
    Your code should not be executed when imported
    The number of elements of argv can be retrieved by using: len(argv)
    You do not have to fully understand lists yet,
        but imagine that argv can be used just like a C array: you can use an index to walk through it.
            There are other ways (which will be preferred for future project tasks),
                if you know them you can use them.
"""
