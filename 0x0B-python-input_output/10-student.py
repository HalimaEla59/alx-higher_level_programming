#!/usr/bin/python3
"""class that defines a Student"""


class Student:
    """representing a student"""

    def __init__(self, first_name, last_name, age):
        """initialising a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary represenation of student"""
        return self.__dict__
