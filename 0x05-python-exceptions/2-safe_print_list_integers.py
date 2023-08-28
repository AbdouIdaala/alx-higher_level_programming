#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for n in my_list:
        length += 1
    try:
        count = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                count += 1
    except IndexError:
        return count
    else:
        return count
    finally:
        print()
