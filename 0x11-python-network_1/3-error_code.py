#!/usr/bin/python3
"""
    Takes a URL
    Sends a request to the URL
    And displays the body of the response(decoded in utf-8)
"""
import urllib, sys

def urlerror_manager(url):
    """
        Manages errors
        Uses the urllib.error.HTTPError
        Takes URL as parameter
    """
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    urlerror_manager(sys.argv[1])