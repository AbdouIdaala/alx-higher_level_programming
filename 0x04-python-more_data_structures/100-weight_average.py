#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    wieghts = 0
    scors = 0
    for t in my_list:
        scors += t[0] * t[1]
        wieghts += t[1]
    return scors / wieghts
