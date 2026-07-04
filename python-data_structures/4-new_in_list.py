#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    area = my_list[:]
    area[idx] = element
    if idx < 0 or idx >= len(my_list):
        return area
    else:
        return area
