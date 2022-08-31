#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ replaces all occurences of an element in a list """
    new_list = my_list.copy()
    idx = 0
    for i in new_list:
        if i == search:
            new_list[idx] = replace
        else:
            idx += 1
            continue
        idx += 1

    return new_list
