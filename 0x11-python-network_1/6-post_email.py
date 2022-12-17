#!/usr/bin/python3
"""Check status"""
import requests
import sys


def post(url, email):
    """status"""
    result = requests.post(url, data={"email": email})

    print(result.text)

if __name__ == "__main__":
    post(sys.argv[1], sys.argv[2])