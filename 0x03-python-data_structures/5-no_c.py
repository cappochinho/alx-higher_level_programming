#!/usr/bin/python3

def no_c(my_string) -> str:
    """Remove all c or C from string"""
    new_string = ""
    for s in my_string:
        if s == "c" or s == "C":
            continue
        new_string += s

    return new_string
