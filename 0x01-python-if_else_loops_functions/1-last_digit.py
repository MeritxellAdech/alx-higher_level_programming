#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "Last digit of"
last = number % 10 if number > 0 else number % (-10)
if last > 5:
    print("{} {} is {:d} and is greater than 5".format(s, number, last))
elif last < 6 and last != 0:
    print("{} {} is {:d} and is less than 6 and not 0".format(s, number, last))
else:
    print("{} {} is {} and is 0".format(s, number, last))
