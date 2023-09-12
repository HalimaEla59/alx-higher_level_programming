#!/usr/bin/python3
"""MyInt class inheriting from int"""


class MyInt(int):
    """it has == and != inverted"""

    def __init__(self, value):
        """initialising"""
        self.value = value

    def __eq__(self, value):
        """changing == with !="""
        return self.real != value

    def __ne__(self, value):
        """changing != with =="""
        return self.real == value
