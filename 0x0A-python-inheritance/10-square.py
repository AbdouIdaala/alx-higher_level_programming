#!/usr/bin/python3
"""import module
"""
Rectangle = __import__('9-rectangle').Rectangle
"""_summary_
"""


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size):
        """_summary_

        Args:
            size (_type_): _description_
        """
        Rectangle.__init__(self, size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size * self.__size
