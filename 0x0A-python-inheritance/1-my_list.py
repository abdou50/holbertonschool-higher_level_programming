#!/usr/bin/python3
""" def medthods"""


class MyList(list):
    """ inherits list from mylist"""
    def print_sorted(self):
        print(sorted(list(self)))
