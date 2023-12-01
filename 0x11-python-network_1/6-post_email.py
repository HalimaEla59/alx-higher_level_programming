#!/usr/bin/python3
"""Sends a POST request passed by URL with email as parameter"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {'email': argv[2]}
    req = requests.post(url, data=mail)
    print(req.text)
