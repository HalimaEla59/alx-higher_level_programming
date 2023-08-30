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
        if(self.position[1]):
            print('' * self.position[1])
        for x in range(self.size):
            if(self.position[0]):
                print(" " * self.position[0], end='')
            print("#" * self.size, end='')
            print()

    def __str__(self):
        if(self.size == 0):
            return ''
        newlines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = "#" * self.size
        return newlines + '\n'.join(spaces + hashes for x in range(self.size))
