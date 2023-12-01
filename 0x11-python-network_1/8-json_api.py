#!/usr/bin/python3
"""Takes in a letter and sends a POSTrequest to http://0.0.0.0:5000..."""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    http = "http://0.0.0.0:5000/search_user"
    req = requests.post(http, data={'q': letter})
    try:
        if req.json():
            reqId = req.json().get('id')
            reqName = req.json().get('name')
            print("[{}] {}".format(reqId, reqName))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
