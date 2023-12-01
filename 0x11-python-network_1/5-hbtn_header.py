#!/usr/bin/python3
"""Displays the value of X-Request-Id in the response header"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    val = 'X-Request-Id'
    print(req.headers.get(val))
