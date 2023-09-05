#!/usr/bin/python3
"""Integer addition function"""


def add_integer(a, b=98):
    """Returns the addition in integer

    Args:
       a (int or float): first number
       b (int or float): second number
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
