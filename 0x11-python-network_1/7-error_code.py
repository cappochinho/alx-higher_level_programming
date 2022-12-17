#!/usr/bin/python3
"""Check status"""
import requests
import sys


def urlerror_code(url):
    """status"""
    result = requests.get(url)
    try:
        if result.status_code > 400:
            print("Error code: {}".format(result.status_code))
        else:
            print(result.content.decode("utf-8"))
    except KeyError:
        pass

if __name__ == "__main__":
    urlerror_code(sys.argv[1])