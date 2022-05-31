#!/usr/bin/python3
""" hihihih """


def write_file(filename="", text=""):
    """write"""
    with open(filename, mode="w", encoding="UTF-8") as lk:
        lk.write(text)
    return len(text)
