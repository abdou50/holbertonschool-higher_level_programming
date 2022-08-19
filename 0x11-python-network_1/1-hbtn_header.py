#!/usr/bin/python3
"""urllib"""
import urllib.request as length
from sys import argv

if __name__ == "__main__":
    with length.urlopen(argv[1]) as response:
        print(response.headers["X-Request-Id"])
