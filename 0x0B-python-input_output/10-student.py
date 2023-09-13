#!/usr/bin/python3
"""class that defines a Student"""


class Student:
    """representing a student"""

    def __init__(self, first_name, last_name, age):
        """initialising a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary represenation of student

        if attrs is list of strings, only what is contained
        in attrs must be retrieved
        """
        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            return ({i: getattr(self, i) for i in attrs if hasattr(self, i)})
        else:
            return self.__dict__
