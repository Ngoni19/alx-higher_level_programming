#!/usr/bin/python3
"""
Script fetches https://alx-intranet.hbtn.io/status
Then displays the response.
"""
import requests

if __name__ == "__main__":
    rq = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(rq.text)))
    print("\t- content: {}".format(rq.text))
