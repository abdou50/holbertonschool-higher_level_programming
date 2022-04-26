#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in (str):
        if ord((i)) >= ord('a') and ord((i)) <= ord('z'):
            new += chr(ord(i) - 32)
        else:
            new += i
    print("{:s}".format(new), end="")
    print("")
