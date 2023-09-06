#!/usr/bin/python3
"""Size validation
"""


class Square:
    """A class Square that defines a square
        Raises:
            TypeError: size must be an int
            ValueError: size must be >= 0
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        pass
