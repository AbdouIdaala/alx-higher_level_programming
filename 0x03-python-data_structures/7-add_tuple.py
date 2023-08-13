#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    a = b = 0
    if (len_a >= 2) or (len_b >= 2):
        if (len_a >= 2) and (len_b < 2):
            if len_b != 0:
                a += tuple_a[0] + tuple_b[0]
                b += tuple_a[1]
            else:
                a += tuple_a[0]
                b += tuple_a[1]
        elif (len_a < 2) and (len_b >= 2):
            if len_a != 0:
                a += tuple_a[0] + tuple_b[0]
                b += tuple_b[1]
            else:
                a += tuple_b[0]
                b += tuple_b[1]
        else:
            a += tuple_a[0] + tuple_b[0]
            b += tuple_a[1] + tuple_b[1]
    else:
        if (len_a != 0) or (len_b != 0):
            if (len_a != 0) and (len_b == 0):
                a += tuple_a[0]
            elif (len_a == 0) and (len_b != 0):
                a += tuple_b[0]
            else:
                a += tuple_a[0] + tuple_b[0]
    new_tuple = (a, b)
    return new_tuple
