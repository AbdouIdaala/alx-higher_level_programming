#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = int(str(number)[len(str(number)) - 1])
if l_digit > 5:
    if number > 0:
        print(f"Last digit of {number} is {l_digit} and is greater than 5")
    else:
        print(f"Last digit of {number} is {-l_digit} and is greater than 5")
elif l_digit < 6 and l_digit != 0:
    if number > 0:
        print(f"Last digit of {number} is {l_digit} \
and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {-l_digit} \
and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {l_digit} and is 0")
