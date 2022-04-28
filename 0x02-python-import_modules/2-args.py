#!/usr/bin/python3
if __name__ == "__main__":
    import sys as n
    num = len(n.argv)
    if num == 1:
        print("{} arguments.".format(0))
    elif num == 2:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(2))

    for i in range(1, num):
        print("{}: {}".format(i, n.argv[i]))
