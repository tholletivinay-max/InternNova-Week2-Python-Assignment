# Import the required modules
import math
import random
import datetime


# 1. Math module
number = float(input("Enter a positive number for square root: "))

if number >= 0:
    print("Square root:", math.sqrt(number))
else:
    print("Please enter a non-negative number.")


# 2. Random module
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)


# 3. Datetime module
current_time = datetime.datetime.now()
print("Current date and time:", current_time)