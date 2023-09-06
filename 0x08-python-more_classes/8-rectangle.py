#!/usr/bin/python3
"""Real definition of a rectangle
"""


class Rectangle:
    """A class that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation

        Args:
            width (int, optional): Defaults to 0.
            height (int, optional): Defaults to 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        self.__class__.number_of_instances += 1
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

    def area(self):
        """Calculate the rectangle area

        Returns:
            int: rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the rectangle perimeter

        Returns:
            int: 0 if width or height == 0, otherwise rectangle permieter
        """
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Print the rectangle with the character '#'

        Returns:
            str: empty string if width or height == 0,\
                otherwise the rectangle with '#' character
        """
        full_str = ""
        if not self.__width or not self.__height:
            return ''
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    full_str += str(self.print_symbol)
                if i < self.__height - 1:
                    full_str += '\n'
        return full_str

    def __repr__(self):
        """A string representation of the rectangle

        Returns:
            str: string representation of the rectangle to be able to \
                recreate a new instance by using eval()
        """
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted
        """
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.__width >= rect_2.__width and rect_1.__height >= rect_2.__height:
            return rect_1
        return rect_2
