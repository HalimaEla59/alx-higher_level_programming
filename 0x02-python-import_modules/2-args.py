i#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(argv) - 1))
    for i in range(len(argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
