#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = {}
    for k, v in a_dictionary.items():
        a[k] = v * 2
        
    return a
