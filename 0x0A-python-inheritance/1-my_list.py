#!/usr/bin/python3
"""MyList inherits from List"""


class MyList(list):
    """prints sorted list"""
    def print_sorted(self):
        print(sorted(self))
