#!/usr/bin/python3
""" Fetches the website https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    """ main function """
    alx = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(alx) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(utf8_content))
