#!/usr/bin/python3
"""
Script takes letter as arg,
POST req to http://0.0.0.0:5000/search_user
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 3:
        LETTER = ""
    else:
        LETTER = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    PayLoad = {'q': LETTER}
    rq = requests.post(url, data=PayLoad)

    try:
        d_01 = rq.json()
        if d_01:
            print("[{}] {}".format(d_01.get('id'), d_01.get('name')))
        else:
            print("No result")
    except ValueError as err:
        print("Not a valid JSON")
