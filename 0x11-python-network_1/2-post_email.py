#!/usr/bin/python3
"""
    Takes a URL and sends an email
    Sends a POST request to the passed URL,
    With email as parameter and
    Displays the body of the response(decoded in utf-8)
"""
import urllib.request as ur
import urllib.parse as pr
import sys

def post(url, email):
    """
        Fetches URL data using two parameters
        url (str): Uniform Resource Locator
        email (str): Email to serve as second parameter
    """
    e = {"email": email}
    data = pr.urlencode(e)
    data = data.encode('ascii')
    req = ur.Request(url, data)
    with ur.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))

if __name__ == "__main__":
    post(sys.argv[1], sys.argv[2])