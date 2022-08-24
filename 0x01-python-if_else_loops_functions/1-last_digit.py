#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
    last_digit = -(-number % 10)
string = "Last digit of {} is {} {}"

if last_digit > 5:
    print(string.format(number, last_digit, "and is greater than 5"))
elif last_digit == 0:
    print(string.format(number, last_digit, "and is 0"))
else:
    print(string.format(number, last_digit, "and is less than 6 and not 0"))
