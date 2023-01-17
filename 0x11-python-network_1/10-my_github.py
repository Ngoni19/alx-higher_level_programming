#!/usr/bin/python3
"""
Script takes GitHub username and password as arg,
Get id from Github api
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    URL = 'https://api.github.com/user'
    rq = requests.get(URL, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(rq.json().get('id'))
