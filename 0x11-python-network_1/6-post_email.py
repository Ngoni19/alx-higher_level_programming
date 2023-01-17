#!/usr/bin/python3
"""
Script takes given URL & email as arg
Sends a POST req to URL,
Display response body utf-8
"""
import requests
from sys import argv

if __name__ == "__main__":
    URL = argv[1]
    var = {'email': argv[2]}
    rq = requests.post(URL, data=var)
    print(rq.text)
