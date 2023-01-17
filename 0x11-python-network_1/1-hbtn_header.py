#!/usr/bin/python3
"""
Script that takes given URL as arg
request URL & display value from reponse header
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    html_req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(html_req) as response:
        print(response.getheader('X-Request-Id'))
