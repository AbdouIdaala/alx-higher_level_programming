#!/usr/bin/python3
"""import module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class."""
    __nb_objects = 0

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size (width and height) of the square.
            x (int, optional): The X coordinate of the square (default is 0).
            y (int, optional): The Y coordinate of the square (default is 0).
            id (int, optional): The ID of the square (default is None).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer (<= 0).
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size
        super().__init__(size, size, x, y, id)
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects
        self.__x = x
        self.__y = y

    def __str__(self):
        """Return a string representation of the square."""
        x_y = f"{self.__x}/{self.__y}"
        return f"[Square] ({self.id}) {x_y} - {self.__size}"

    @property
    def size(self):
        """Get the size (width and height) of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size (width and height) of the square.

        Args:
            value (int): The new size (width and height) of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not a positive integer (<= 0).
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args: Positional arguments in the order: id, size, x, y.
            **kwargs: Keyword arguments for any of the attributes
            (size, x, y, id).
        """
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__size = args[i]
                if i == 2:
                    self.__x = args[i]
                if i == 3:
                    self.__y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.__size = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """Return a dictionary representation of the square.

        Returns:
            dict: A dictionary containing the square's attributes.
        """
        dictionary = {
            'id': self.id,
            'x': self.__x,
            'size': self.__size,
            'y': self.__y,
        }
        return dictionary
