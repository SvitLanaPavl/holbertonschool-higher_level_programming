#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from Base Geometry"""

    def __init__(self, width, height):
        """
        Initialization

        Args:
        width: the width of the rectangle (private)
        height: the height of the rectangle (private)
        """

        # Validate the width and height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of the rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
