#!/usr/bin/python3
"""Prints text with two new lines after .,?:"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    x = 0
    for i, val in enumerate(text):
        if val in '?:.':
            print(text[x:i + 1].strip() + '\n')
            x = i + 1
    if not x:
        print(text, end='')
    elif x is not len(text):
        print(text[x:i + 1].strip(), end='')
