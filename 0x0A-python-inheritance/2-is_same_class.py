#!/usr/bin/python3
"""comapre"""


def is_same_class(obj, a_class):
    """
    Method that comapres an object with a class
    and return a true or false statment
    """
    if type(obj) is a_class:
        return 1 == 1
    else:
        return 1 == 2
