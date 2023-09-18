#!/usr/bin/python3
"""class Square inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """creates a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialising"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """str representation of square"""
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id,
                self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """updates the square"""
        if args and len(args) != 0:
            count = 0
            keys = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, keys[count], arg)
                count += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation"""
        dictionary = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return dictionary
