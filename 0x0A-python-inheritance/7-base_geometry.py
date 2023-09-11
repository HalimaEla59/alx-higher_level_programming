#!/usr/bin/python3
"""base geometry class"""


class BaseGeometry:
    """the class:"""

    def area(self):
        """instance methode not implementes"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator of parameter as int and >"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if type(value) <= 0:
            raise ValueError("{} must be greater than 0".format(name))
