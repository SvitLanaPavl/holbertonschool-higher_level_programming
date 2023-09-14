#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Represents square"""
    __size = None

    def __init__(self, size=0):
        """Initialization of size"""
        self.__size = size

    @property
    def size(self):
        """Get thesize of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setting the size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returning the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
