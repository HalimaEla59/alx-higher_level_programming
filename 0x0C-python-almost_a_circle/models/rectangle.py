#!/usr/bin/python3
"""class Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """creates a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialising"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of wigth"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value = 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x
