#!/usr/bin/python3
"""func returns the list of 
    available attributes and methods
    """

def lookup(obj):
    """list of dir()"""

    return [x for x in dir(obj)]
