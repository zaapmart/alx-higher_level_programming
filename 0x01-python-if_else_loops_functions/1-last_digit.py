#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
message = "Last digit of"
if number > 5:
    print(f"{message} {number} is {lastDigit} and is greater than 5")
elif number == 0:
    print(f"{message} {number} is {lastDigit} and is 0")
elif number < 6:
    print(f"{message} {number} is {lastDigit} and is less than 6 and not 0")

