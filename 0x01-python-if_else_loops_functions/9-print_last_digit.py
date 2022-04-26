#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        l = abs(number)
    else:
        l = number 
    print(l % 10, end="")
    return (l % 10)
