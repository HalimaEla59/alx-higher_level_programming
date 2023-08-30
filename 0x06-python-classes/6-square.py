#!/usr/bin/python3

"""define a class named Square"""


class Square:
    """instantination with optional size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square

        Args:
           size(int): size of the square
           position(int, int): the position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of position"""
        if ((type(value) is not tuple) or (len(value) is not 2) or
                (type(value[0]) is not int) or
                (type(value[1]) is not int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0) or (value[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value
  
    def area(self):
        """returns the area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints square of # with position and size"""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
