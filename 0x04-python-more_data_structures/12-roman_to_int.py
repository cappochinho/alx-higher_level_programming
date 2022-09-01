#!/usr/bin/python3

def roman_to_int(roman_string):
    """ converts from roman numeral to int """
    if not isinstance(roman_string, str):
        return 0
    all = 0
    num = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for n in reversed(roman_string):
        num = digits[n]
        all += num if all < num * 5 else -num
    return all
