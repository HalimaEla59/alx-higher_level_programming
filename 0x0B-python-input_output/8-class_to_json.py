#!/usr/bin/python3
"""returns dictionary description with simple data"""


def class_to_json(obj):
    """for JSON serialistaion of an object"""
    return obj.__dict__
