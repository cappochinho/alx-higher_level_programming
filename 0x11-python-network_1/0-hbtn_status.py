#!/usr/bin/python3
'''
    Fetches a specified URL
'''
import urllib.request as ur

def url_fetcher(source):
    '''
        Fetches url data
        url(string): the Uniform Resource Locator
    '''
    with ur.urlopen(source) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t-utf8 content: {}'.format(html.decode("utf-8")))

if __name__ == '__main__':
    url_fetcher('https://alx-intranet.hbtn.io/status')