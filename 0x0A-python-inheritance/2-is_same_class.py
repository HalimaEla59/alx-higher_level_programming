#!/usr/bin/python3
"""checks if object is exactly an instance
   of the specified class"""

def is_same_class(obj, a_class):
    """True or False"""
    return type(obj) is a_class
