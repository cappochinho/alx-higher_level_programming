#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers in matrix """
    new = []
    for list in matrix:
        temp = []
        for i in list:
            temp.append(i ** 2)
        new.append(temp)

    return new
