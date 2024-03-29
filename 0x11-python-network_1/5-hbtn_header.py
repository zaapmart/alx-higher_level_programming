#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the
response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python script.py <URL>")
    else:
        url = argv[1]
        try:
            r = requests.get(url)
            r.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
            r_id = r.headers.get('X-Request-Id')
            if r_id:
                print(r_id)
            else:
                print("X-Request-Id header not found in the response.")
        except requests.RequestException as e:
            print("Error occurred while fetching the URL:", e)
