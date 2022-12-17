#!/usr/bin/python3
"""
    Displays the value of the variable
    X-Request-Id key in the response header
"""

import requests, sys

def url_field(url):
    """
        Displays the request id of a response header
        Params: url
    """

    result = requests.get(url)

    print(result.headers.get("X-Request-Id", None))

if __name__ == "__main__":
    url_field(sys.argv[1])