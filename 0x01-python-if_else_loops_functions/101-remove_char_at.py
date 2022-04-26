#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    if n >= 0:
        new += str[:n]
        new += str[n+1:]
    else:
        new = str
    return new
