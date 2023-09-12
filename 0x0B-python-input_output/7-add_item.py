#!/usr/bin/python3
"""adds all args to python list and saves them as file"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    jList = load_from_json_file("add_item.json")
except:
    jList = []
jList.extend(sys.argv[1:])
save_to_json_file(jList, "add_item.json")
