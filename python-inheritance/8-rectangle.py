#!/usr/bin/python3
"""Geometry module"""
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
        self.__width = width
        self.__height = height

        # Validate the width and height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
