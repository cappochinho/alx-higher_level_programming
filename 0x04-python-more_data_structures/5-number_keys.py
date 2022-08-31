#!/usr/bin/python3

def number_keys(a_dictionary):
    """ finds the number of key in a dictionary """
    key_count = 0
    for _key in a_dictionary.keys():
        key_count += 1

    return key_count
