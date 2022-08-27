#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Add new element to list copy"""
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
