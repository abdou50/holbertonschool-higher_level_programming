#!/usr/bin/python3

def switch():
    a = 89
    b = 10
    aux = a
    a = b
    b = aux
    print("a={:d} - b={:d}".format(a, b))
