#!/usr/bin/python3
"""This module defines a square."""


class Square:
    """It represents a square."""
    __size = None

    def __init__(self, size=0):
        """Initializing the size"""
        self.__size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns current square area"""
        return self.__size * self.__size
