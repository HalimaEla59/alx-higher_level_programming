#!/usr/bin/python3
"""Prints 10 commits from a user s github repo"""
import sys
import requests


if __name__ == "__main__":
    user = sys.argv[2]
    repo = sys.argv[1]
    req = requests.get("https://api.github.com/repos/{}/{}/commits"
            .format(user, repo))
    commits = req.json()
    for c in commits[:10]:
        print(c.get('sha'), end=': ')
        print(c.get('commit').get('author').get('name'))
