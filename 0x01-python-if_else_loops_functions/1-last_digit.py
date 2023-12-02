#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last = number % 10
if last > 5:
    print(f'Last digit of %d is %d and is greater than 5' % (number))
elif last == 0:
    print('Last digit of %d is %d and is 0' % (number, last))
else:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
