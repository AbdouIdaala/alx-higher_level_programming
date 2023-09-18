#!/usr/bin/python3
"""import module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base class."""
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The X coordinate of the rectangle
            (default is 0).
            y (int, optional): The Y coordinate of the rectangle
            (default is 0).
            id (int, optional): The ID of the rectangle (default is None).

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width, height, x, or y is not a positive
            integer (<= 0).
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not a positive integer (<= 0).
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not a positive integer (<= 0).
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x of the rectangle.

        Args:
            value (int): The new x of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not a positive integer (< 0).
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y of the rectangle.

        Args:
            value (int): The new y of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not a positive integer (< 0).
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__x = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle by printing it to the console.

        The rectangle is printed with proper indentation
        (self.__x) and height (self.__height).
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x, end=('#' * self.__width))
            print()

    def __str__(self):
        """Return a string representation of the rectangle."""
        x_y = f"{self.__x}/{self.__y}"
        width_height = f"{self.__width}/{self.__height}"
        return f"[Rectangle] ({self.id}) {x_y} - {width_height}"

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.

        Args:
            *args: Positional arguments in the order: id, width, height, x, y.
            **kwargs: Keyword arguments for any of the attributes
            (width, height, x, y, id).
        """
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle.

        Returns:
            dict: A dictionary containing the rectangle's attributes.
        """
        dictionary = {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
        }
        return dictionary
