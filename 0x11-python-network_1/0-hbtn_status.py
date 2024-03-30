#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content.decode('utf-8')))
