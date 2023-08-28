#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    length = 0
    for n in my_list:
        length += 1
    try:
        for i in range(x):
            print(my_list[i], end='')
        return x
    except IndexError:
        return length
    finally:
        print()
