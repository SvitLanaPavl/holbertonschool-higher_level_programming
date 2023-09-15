#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Represents square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getting the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setting the size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Getting position"""
        return self.__position

    @position.setter
    def position(self, position):
        """Setting position"""
        if not isinstance(position, tuple) and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if all(isinstance(elem, int) and elem >= 0 for elem in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Returning the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
