#!/usr/bin/python3
"""Takes github user and pw and uses GitHub API to display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    user = sys.argv[1]
    pw = sys.argv[2]
    a = HTTPBasicAuth(user, pw)
    http = "https://api.github.com/user"
    req = requests.get(http, auth=a)
    print(req.json().get("id"))
