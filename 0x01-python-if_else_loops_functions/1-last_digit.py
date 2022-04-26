#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
k = abs(number)
n = k % 10
if number < 0:
    n = -n
print("Last digit of {} ".format(number, n) end="")
if n > 5:
    print("greater than 5")
elif n == 0:
    print("0")
else:
    print("less than 6 and not 0")
