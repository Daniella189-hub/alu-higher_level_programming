#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    area = my_list[:]
    if idx < 0 and idx >= len(my_list):
        return area
    area[idx] = element
    return area
