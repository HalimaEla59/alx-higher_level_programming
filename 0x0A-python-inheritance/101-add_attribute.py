#!/usr/bin/python3
"""func adding attributes or objects"""


def add_attribute(obj, attr, value):
    """addes new attributes/object"""
    if not hasattr(obj, "__dir__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
