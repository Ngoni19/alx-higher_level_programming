#!/usr/bin/python3
"""
Script takes given URL as arg,
req URL then  display from reponse header
"""
import requests
from sys import argv


if __name__ == "__main__":
    rq = requests.get(argv[1])
    print(rq.headers.get('X-Request-Id'))
