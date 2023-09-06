#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last = number % 10

greater = "and is greater than 5"
zero = "and is 0"
less = "and is less than 6 and not 0"

if last > 5:
    print("Last digit of {} is {} {}".format(number, last, greater))
elif last == 0:
    print("Last digit of {} is {} {}".format(number, last, zero))
else:
    print("Last digit of {} is {} {}".format(number, last, less))