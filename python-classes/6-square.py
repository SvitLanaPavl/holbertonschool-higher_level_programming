#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Represents square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of size and position

        Args:
        size(int): the size of the new square
        position(int, int): the position of the new square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getting the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getting position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting position"""
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if all(isinstance(elem, int) and elem >= 0 for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returning the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        elif self.__position is None:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
