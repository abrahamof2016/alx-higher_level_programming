#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_dig = -1 * number % 10
    last = -1 * last_dig
    if last == 0:
        print(f"Last digit of {number} is {las} and is 0")
    elif last < 0:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif number >= 0:
    lad = number % 10
    if (lad == 0):
        print(f"Last digit of {number} is {lad} and is 0")
    elif (lad < 6 and last_dig > 0):
        print("Last digit of {number} is {lad} and is less than 6 and not 0")
    elif (lad > 5):
        print(f"Last digit of {number} is {lad} and is greater than 5")
