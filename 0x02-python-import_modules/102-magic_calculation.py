#!/usr/bin/python3
import dis


def compare(a, b):
    a = 0
    if a < b:
        return b
    return a


dis.dis(compare)
