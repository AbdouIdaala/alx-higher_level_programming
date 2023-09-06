#!/usr/bin/python3
"""Size validation
"""


class Square:
    """A class Square that defines a square
        Raises:
            TypeError: size must be an int
            ValueError: size must be >= 0
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position
        pass

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
        if self.__size == 0:
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        err_msg = "position must be a tuple of 2 positive integers"
        if isinstance(value, tuple):
            if len(value) == 2:
                if not isinstance(value[0], int) and not isinstance(value[1], int):
                    raise TypeError(err_msg)
            else:
                raise TypeError(err_msg)
        else:
            raise TypeError(err_msg)
        self.__position = value
