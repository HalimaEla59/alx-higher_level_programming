#!/usr/bin/python3
"""Takes in a URL, sends request to URL, displays the body of response"""
import sys
import urllib.request
import urllib.parse
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
