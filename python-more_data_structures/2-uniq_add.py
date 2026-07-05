#!/usr/bin/python3
def uniq_add(my_list=[]):
    for i in sorted(set(my_list)):
        a = sum(set(my_list))
        return a
