#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    area = my_list[:]
    if idx < 0 or idx >= len(area):
        return area
    area[idx] = element
    return area
