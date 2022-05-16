#!/usr/bin/python3
def safe_print_division(a, b):
    count = 0
    try:
        count = a/b
    except ZeroDivisionError:
        count = None
    finally:
        print("Inside result: {}".format(x))
        return count
