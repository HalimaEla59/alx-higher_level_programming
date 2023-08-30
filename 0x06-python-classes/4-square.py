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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
  
    def area(self):
        """returns the area of square"""
        return (self.__size * self.__size)
