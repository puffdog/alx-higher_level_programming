#!/usr/bin/python3
import random
number = random.uniform(-1, 1)
# Print whether the number is positive or negative
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
