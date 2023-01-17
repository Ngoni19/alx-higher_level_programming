#!/usr/bin/python3
"""
Script takes given URL & email as arg,
Send POST html_req to URL -> display response body utf-8
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    URL = argv[1]
    var = {'email': argv[2]}

    d = urllib.parse.urlencode(var)
    d = d.encode('ascii')
    html_req = urllib.request.Request(URL, d)
    with urllib.request.urlopen(html_req) as response:
        print(response.read().decode('utf-8'))
