#!/usr/bin/python3
"""
    Fetches a specified URL
"""

import requests

def url_fetcher(url):
    """
        Uses the requests package

        url(str): The URL string
    """
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == "__main__":
    url_fetcher("https://alx-intranet.hbtn.io/status")