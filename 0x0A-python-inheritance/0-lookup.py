#!/usr/bin/python3
"""return list of attributes/methods"""


def lookup(obj):
    """list of dir()"""
    return [x for x in dir(obj)]
