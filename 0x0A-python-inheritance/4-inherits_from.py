#!/usr/bin/python3
"""class"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and type(obj) != a_class:
        return 1 == 1
    else:
        return 1 == 2
