#!/usr/bin/python3
import urllib.request as length

if __name__ == "__main__":
    with length.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
