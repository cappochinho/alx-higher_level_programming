#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """ deletes a key in a dictionary """
    for i in a_dictionary.keys():
        if key == i:
            del a_dictionary[key]
            break
        continue

    return a_dictionary
