#!/usr/bin/python3
""" hihihih """


def read_file(filename=""):
    """readfile"""
    with open(filename, mode="r", encoding="UTF-8") as no:
        print (no.read(), end="")
