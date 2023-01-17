#!/usr/bin/python3
"""
Script takes given URL & email as arg,
Display response body utf-8 then print error codes
"""
import requests
from sys import argv


if __name__ == "__main__":
    rq = requests.get(argv[1])
    if rq.status_code >= 400:
        print("Error code: {}".format(rq.status_code))
    else:
        print(rq.text)
