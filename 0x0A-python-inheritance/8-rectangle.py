#!/usr/bin/python3
"""import module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""_summary_
"""


class Rectangle(BaseGeometry):
    """_summary_

    Args:
        BaseGeometry (_type_): _description_
    """

    def __init__(self, width, height):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
        """
        BaseGeometry.integer_validator(self, width, width)
        BaseGeometry.integer_validator(self, height, height)
        self.__width = width
        self.__height = height
