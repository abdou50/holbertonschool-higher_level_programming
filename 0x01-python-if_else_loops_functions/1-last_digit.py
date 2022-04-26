#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
k = abs(number)
n = k % 10
if number < 0:
    n = -n
if n < 6 and n != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, n))
elif n == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, n))
else:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, n))
