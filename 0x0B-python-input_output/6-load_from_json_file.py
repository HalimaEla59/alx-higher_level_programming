#!/usr/bin/python3
"""creates an object from JSON file"""
import json


def load_from_json_file(filename):
    """the function:"""
    with open(filename) as f:
        return json.load(f)
