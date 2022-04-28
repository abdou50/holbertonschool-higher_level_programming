#!/usr/bin/python3
if __name__ == "__main__":
    import sys as m

    a = 0
    for i in range(len(m.argv) - 1):
        a += int(m.argv[i + 1])
    print("{}".format(a))
