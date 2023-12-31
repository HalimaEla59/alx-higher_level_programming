#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle

    Attributes:
        number_of_instances (int): number of instances
        print_symbol (any): used symbole for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Prints the rectangle with hashtags"""
        if not self.perimeter():
            return ""
        return ('\n'.join("{}".format(
            self.print_symbol) * self.__width for i in range(self.__height)))

    def __repr__(self):
        """Returns string representation of rectangle"""
        output = "Rectangle(" + str(self.__width)
        output += ", " + str(self.__height) + ")"
        return output

    def __del__(self):
        """Message deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with bigger area

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        """
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new rectangle instance width=height=size

        Args:
           size (int): width and height
        """
        return cls(size, size)
