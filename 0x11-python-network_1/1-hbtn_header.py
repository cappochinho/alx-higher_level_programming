#!/usr/bin/python3
"""
    Takes a URL
    Sends a request to the URL
    Displays the value of the X-Request-Id
"""
import urllib.request as ur
import sys

def url_fetcher(source):
    """
        Fetches a URL
    """
    with ur.urlopen(source) as response:
        html = response.info().get("X-Request-Id")
        print(html)

if __name__ == "__main__":
    url_fetcher(sys.argv[1])