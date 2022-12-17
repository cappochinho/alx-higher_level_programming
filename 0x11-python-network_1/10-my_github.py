#!/usr/bin/python3
"""Check status"""
import requests
from requests.auth import HTTPBasicAuth
import sys


def searchapi(uname, pwd):
    """status"""
    user = uname
    pw = pwd
    result = requests.get("https://api.github.com/user",
                          auth=(HTTPBasicAuth(user, pw)))

    try:
        data = result.json()
        print(data["id"])
    except:
        print("None")

if __name__ == "__main__":
    searchapi(str(sys.argv[1]), str(sys.argv[2]))