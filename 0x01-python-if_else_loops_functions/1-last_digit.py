#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[len(str(number)) - 1])
msg = f"Last digit of {number} is {last_digit} "
if last_digit > 5:
    msg += "and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    msg += "and is less than 6 and not 0"
else:
    msg += "and is 0"
print(msg)
