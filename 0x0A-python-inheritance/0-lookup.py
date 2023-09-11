#!/usr/bin/python3
"""returns list of attributes and methods"""



def lookup(obj):
    """list of dir()"""
    return [x for x in dir(obj)]
