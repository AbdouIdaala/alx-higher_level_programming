#!/usr/bin/python3
"""_summary_
"""


def add_integer(a, b=98):
    """Returns an the addition of (a + b)

    Args:
        a: int or float.
        b: int or float. Defaults to 98.
    a and b must be first casted to integers if they are float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
