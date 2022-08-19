#!/usr/bin/python3
"""urllib"""
from urllib import request, parse
from sys import argv
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError:
        print('Error code: {}'.format(HTTPError.code))
