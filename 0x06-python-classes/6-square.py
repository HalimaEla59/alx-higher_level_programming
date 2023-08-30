#!/usr/bin/python3

"""define a class named Square"""

class Square:
    """instantination with optional size"""

    def __init__(self, size=0):
        """Initializes a new square

        Args:
           __size(int): size of the square
           must be positive and integer
        """
        self.__size = size

    @property
    def size(self):
        """getter the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
  
    def area(self):
        """returns the area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints size"""
        for i in range(self.__size):
            print("#" * self.__size, end="")
            print()
        if self.__size == 0:
            print()
