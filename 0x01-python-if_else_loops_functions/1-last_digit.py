#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = number % 10
if last_dig > 5:
    print("last digit of {} is {} and is greater than 5"
          .format(number, last_dig))
elif last_dig == 0:
    print("last digit of {} is {} and is 0".format(number, last_dig))
elif last_dig < 6 and last_dig != 0:
    print("last digit of {} is {} and is less than 6 and not 0"
          .format(number, last_dig))
