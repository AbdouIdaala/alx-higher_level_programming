#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = length = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                count += 1
            length += 1
    except IndexError:
        return length
    else:
        return count
    finally:
        print()
