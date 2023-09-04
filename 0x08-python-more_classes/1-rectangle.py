#!/usr/bin/python3
"""Real definition of a rectangle
"""


class Rectangle:
    """A class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """Instantiation

        Args:
            width (int, optional): Defaults to 0.
            height (int, optional): Defaults to 0.
        """
        self.__width = width
        self.__height = height
        pass

    @property
    def width(self):
        """Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Check width value

        Args:
            value (int): width value

        Raises:
            TypeError: width must be an integer
            ValueError: width < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Check height value

        Args:
            value (int): height value

        Raises:
            TypeError: height must be an integer
            ValueError: height < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
