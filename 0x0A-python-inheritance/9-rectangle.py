#!/usr/bin/python3
"""class rectangle inherits fromBaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle uses  BaseGeometry"""

    def __init__(self, width, height):
        """initialising:"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
