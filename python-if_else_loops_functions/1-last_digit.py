#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if number > 0:
    if str(number)[-1] > "5":
        print(f"Last digit of {str(number)} is {str(number)[-1]} and is greater than 5")
    elif str(number)[-1] == "0":
        print(f"Last digit of {str(number)} is {str(number)[-1]} and is 0")
    elif str(number)[-1] != "0" and str(number)[-1] < "6":
        print(f"Last digit is {str(number)} is {str(number)[-1]}  and is less than 6 and not 0")
    else:
        print("Last digit unrecognised")
elif number < 0:
    last_digit = -last_digit
    if last_digit > -5:
        print(f"Last digit of {str(number)} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"Last digit of {str(number)} is {last_digit} and is 0")
    elif last_digit != 0 and last_digit < -6:
        print(f"Last digit is {str(number)} is {last_digit  and is less than 6 and not 0")
else:
    print("shift")
