#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectanle class representation"""
    def __init__(self, width=0, height=0):
        """Initialization of properties

        Args:
        width - width, must be an integer
        height - height, must be an integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
