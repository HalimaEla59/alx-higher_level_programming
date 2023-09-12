#!/usr/bin/python3
"""writes a str to a text file"""


def write_file(filename="", text=""):
    """returns the number of characters"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
