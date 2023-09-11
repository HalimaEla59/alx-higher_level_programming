#!/usr/bin/python3
"""if obj is instance of class inherited from specified class"""


def inherits_from(obj, a_class):
    """returns True or False"""
    if tpe(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
