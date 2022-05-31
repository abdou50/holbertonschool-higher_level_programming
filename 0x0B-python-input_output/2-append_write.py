#!/usr/bin/python3
""" hihihih """


def append_write(filename="", text=""):
    """class"""
    with open(filename, mode="a", encoding="UTF-8") as ka:
        ka.write(text)
    return len(text)
