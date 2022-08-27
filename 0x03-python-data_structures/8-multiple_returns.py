#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns string length and first character"""
    multi_return = (0, "None")

    if len(sentence) == 0:
        return multi_return

    multi_return = (len(sentence), sentence[:1])
    return multi_return
