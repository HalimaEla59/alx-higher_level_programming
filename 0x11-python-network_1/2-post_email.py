#!/usr/bin/python3
"""Takes in a URL and email, sends POST request to URL with email as param"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(mail).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
