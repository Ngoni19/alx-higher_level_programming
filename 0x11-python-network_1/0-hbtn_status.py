#!/usr/bin/python3
"""
The script uses ;
fetch https://alx-intranet.hbtn.io/status -> display response
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        d_html = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(d_html)))
        print("\t- content: {}".format(d_html))
        print("\t- utf8 content: {}".format(d_html.decode('utf-8')))
