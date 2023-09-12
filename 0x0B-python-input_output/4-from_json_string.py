#!/usr/bin/python3
"""JSON to python object func"""
import json


def from_json_string(my_str):
    """returns py object representation of JSON str"""
    return json.loads(my_str)
