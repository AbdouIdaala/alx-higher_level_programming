#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        for i in range(b):
            result *= a
    else:
        i = b
        while i < 0:
            result /= 10
            i += 1
    return result
