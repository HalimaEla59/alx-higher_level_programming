#!/usr/bin/python3
"""writes object to text file with JSON"""
import json


def save_to_json_file(my_obj, filename):
    """writes with JSON representation"""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
