#!/usr/bin/python3
"""text file reading function"""


def read_file(filename=""):
    """prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
