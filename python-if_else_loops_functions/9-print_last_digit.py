#!/usr/bin/python3
def print_last_digit(number):
    number= str(number)
    last_digit= int(str(number[-1]))
    print(f"{last_digit}", end="")
    return last_digit
