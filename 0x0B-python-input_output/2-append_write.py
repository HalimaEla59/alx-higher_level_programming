#!/usr/bin/python3
"""appends a str at the end of text file"""


def append_write(filename="", text=""):
    """returns the nember of characters"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
