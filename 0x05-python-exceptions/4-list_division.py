#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new = []
    while i < list_length:
        result_list = 0
        try:
            result_list = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new.append(result_list)
            i += 1
    return new
