#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    count = 0
    while length < x:
        try:
            print("{:d}".format(my_list[length]), end="")
            length += 1
            count += 1
        except (TypeError, ValueError):
            length += 1
    print()
    return(count)
