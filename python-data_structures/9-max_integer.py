#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return my_list.pop()
    else:
        my_list.sort()
        return my_list.pop()
