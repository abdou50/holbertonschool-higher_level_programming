#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    for i in my_list:
        try:
            while(length < x):
                print("{}".format(my_list[length]), end="")
                length += 1
        except IndexError:
            None
    print()
    return (length)
