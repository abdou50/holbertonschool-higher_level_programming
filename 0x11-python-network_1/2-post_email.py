#!/usr/bin/python3
"""urllib"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    linux = parse.urlencode({'email': argv[2]}).encode('utf-8')
    with request.urlopen(argv[1], linux) as length:
        print(length.read().decode('utf-8'))
