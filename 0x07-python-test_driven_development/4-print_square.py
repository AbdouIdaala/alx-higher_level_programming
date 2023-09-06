#!/usr/bin/python3
"""_summary_
"""


def print_square(size):
    """Print a square with the character #

    Args:
        size (int): size length of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
