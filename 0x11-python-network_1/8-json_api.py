#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://localhost:5000/api/v1/stats with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    takes in a letter and sends a POST request to
    http://localhost:5000/api/v1/stats with the letter as a parameter
    """
    url = 'http://localhost:5000/api/v1/stats'
    if len(argv) == 2:
        letter = argv[1]
    else:
        letter = ""
        
    try:
        r = requests.post(url, data={'q': letter})
        response_json = r.json()
        if response_json:
            if 'id' in response_json and 'name' in response_json:
                print("[{}] {}".format(response_json['id'], response_json['name']))
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except requests.RequestException as e:
        print("Error occurred while making the request:", e)
